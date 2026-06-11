#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генерация печатного PDF коммерческого предложения 1ОС.ЭДО.Легаси."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "kp-1os-edo-legasi.pdf"

FONT_CANDIDATES = {
    "regular": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ],
    "bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ],
}


def resolve_font(kind: str) -> str:
    for path in FONT_CANDIDATES[kind]:
        if Path(path).is_file():
            return path
    raise FileNotFoundError(
        "Не найден шрифт с кириллицей. Установите DejaVu Sans "
        "или проверьте наличие Arial в системе."
    )


def main() -> None:
    pdfmetrics.registerFont(TTFont("DejaVu", resolve_font("regular")))
    pdfmetrics.registerFont(TTFont("DejaVuBd", resolve_font("bold")))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=18 * mm,
        bottomMargin=20 * mm,
        title="Коммерческое предложение — 1ОС.ЭДО.Легаси",
        author="First Open Systems",
    )

    base = getSampleStyleSheet()
    normal = ParagraphStyle(
        "RU",
        parent=base["Normal"],
        fontName="DejaVu",
        fontSize=10.5,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=base["Heading1"],
        fontName="DejaVuBd",
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=14,
        textColor=colors.HexColor("#1a2744"),
    )
    h2 = ParagraphStyle(
        "H2",
        parent=base["Heading2"],
        fontName="DejaVuBd",
        fontSize=12,
        leading=16,
        spaceBefore=12,
        spaceAfter=8,
        textColor=colors.HexColor("#1a2744"),
    )
    small = ParagraphStyle(
        "Small",
        parent=normal,
        fontSize=9,
        leading=12,
        textColor=colors.grey,
        alignment=TA_CENTER,
        spaceBefore=8,
    )

    story: list = []

    story.append(Paragraph("КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ", h1))
    story.append(Paragraph("Приложение <b>1ОС.ЭДО.Легаси</b>", h1))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Интеграция учётной системы с оператором электронного документооборота "
            "<b>ЭДО Доки</b> (компания «Астрал») для обмена юридически значимыми "
            "электронными документами с контрагентами.",
            normal,
        )
    )
    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph("1. Назначение продукта", h2))
    story.append(
        Paragraph(
            "Приложение предназначено для организаций, которым требуется связать "
            "привычные процессы в учётной системе с оператором ЭДО Доки без избыточной "
            "ручной работы и дублирования документов в веб-кабинетах.",
            normal,
        )
    )

    story.append(Paragraph("2. Ключевые возможности", h2))
    bullets = ListFlowable(
        [
            ListItem(
                Paragraph(
                    "<b>Исходящие УПД.</b> Отправка универсальных передаточных документов "
                    "контрагентам минимальным числом действий («в одно касание»).",
                    normal,
                ),
                leftIndent=12,
                bulletColor=colors.HexColor("#2563eb"),
            ),
            ListItem(
                Paragraph(
                    "<b>Входящие документы и счёт-фактуры.</b> Создание счёт-фактур "
                    "по входящим электронным документам с учётом логики вашей конфигурации.",
                    normal,
                ),
                leftIndent=12,
                bulletColor=colors.HexColor("#2563eb"),
            ),
            ListItem(
                Paragraph(
                    "<b>Подписание в интерфейсе Доки.</b> Документы, требующие подписи, "
                    "отображаются в разделе «Черновики» веб-интерфейса ЭДО Доки.",
                    normal,
                ),
                leftIndent=12,
                bulletColor=colors.HexColor("#2563eb"),
            ),
            ListItem(
                Paragraph(
                    "<b>ЭПД и ЭТрН.</b> Синхронизация электронных перевозочных документов "
                    "с оператором: реестр «Логистика», просмотр ЭТрН, импорт и подписи "
                    "через API раздела EPD.",
                    normal,
                ),
                leftIndent=12,
                bulletColor=colors.HexColor("#2563eb"),
            ),
            ListItem(
                Paragraph(
                    "<b>Несколько организаций.</b> Поддержка работы с несколькими "
                    "организациями в одной базе учётной системы.",
                    normal,
                ),
                leftIndent=12,
                bulletColor=colors.HexColor("#2563eb"),
            ),
        ],
        bulletType="bullet",
        start="•",
    )
    story.append(bullets)
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("3. Интеграция и внедрение", h2))
    story.append(
        Paragraph(
            "Подключение к учётной системе выполняется посредством "
            "<b>динамически подключаемого модуля</b>, что позволяет ограничить объём "
            "изменений в конфигурации и снизить риски для рабочей базы по сравнению "
            "с глубокой встройкой в типовой код.",
            normal,
        )
    )
    story.append(
        Paragraph(
            "Архитектура приложения рассчитана на быстрое добавление нового функционала "
            "и поддержку широкого спектра конфигураций, в том числе снятых с официальной "
            "поддержки производителя.",
            normal,
        )
    )

    story.append(Paragraph("4. Сценарии и развитие", h2))
    story.append(
        Paragraph(
            "Поддерживаются современные сценарии на модифицированных конфигурациях, "
            "включая обмен УПД, работу с <b>кодами маркировки</b> и "
            "<b>электронными перевозочными документами (ЭПД)</b>, в том числе ЭТрН. "
            "Обмен с оператором реализован через API раздела EPD.",
            normal,
        )
    )
    story.append(
        Paragraph(
            "Решение позволяет автоматизировать рутинные операции и ускорить обработку "
            "документооборота между учётом и оператором ЭДО.",
            normal,
        )
    )

    story.append(Paragraph("5. Лицензия и стоимость", h2))
    story.append(
        Paragraph(
            "Стоимость лицензии составляет <b>50&nbsp;000 (пятьдесят тысяч) рублей в год</b> "
            "включая НДС по действующей ставке (если применимо) — уточняется в договоре.",
            normal,
        )
    )
    story.append(
        Paragraph(
            "В лицензию входят: <b>первоначальная настройка</b> интеграции с ЭДО Доки и "
            "<b>исправление ошибок</b> в рамках согласованного объёма сопровождения. "
            "Итоговый перечень работ и условия фиксируются в договоре.",
            normal,
        )
    )

    story.append(Paragraph("6. Контакты", h2))
    story.append(
        Paragraph(
            "По вопросам приобретения лицензии, демонстрации и согласования условий "
            "внедрения обращайтесь в Telegram: <b>@FirstOpenSystems</b> "
            "(https://t.me/FirstOpenSystems).",
            normal,
        )
    )

    story.append(Spacer(1, 10 * mm))
    story.append(
        Paragraph(
            "Документ носит информационный характер и не является публичной офертой. "
            "ЭДО Доки — продукт компании «Астрал».",
            small,
        )
    )

    doc.build(story)
    print(f"Written: {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
