from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame

# Colors
DARK_BLUE = colors.HexColor('#2C4A7C')
LIGHT_BLUE = colors.HexColor('#EEF2F8')
CREAM = colors.HexColor('#F8F6F1')
DARK_TEXT = colors.HexColor('#1A1A2E')
MID_TEXT = colors.HexColor('#444444')
LIGHT_TEXT = colors.HexColor('#888888')
ACCENT = colors.HexColor('#E8A020')
WHITE = colors.white

W, H = A4

class OnePagerPDF:
    def __init__(self, path):
        self.path = path
        self.c = canvas.Canvas(path, pagesize=A4)
        self.width = W

    def draw_header(self):
        # Left blue panel
        self.c.setFillColor(DARK_BLUE)
        self.c.rect(0, H - 180, 180, 180, fill=1, stroke=0)

        # Header text on blue
        self.c.setFillColor(WHITE)
        self.c.setFont("Helvetica-Bold", 28)
        self.c.drawString(24, H - 80, "傅小凡")
        self.c.setFont("Helvetica", 11)
        self.c.drawString(24, H - 105, "厦门大学 MBA中心")
        self.c.drawString(24, H - 120, "教授 · 博士生导师")

        # Accent line
        self.c.setStrokeColor(ACCENT)
        self.c.setLineWidth(3)
        self.c.line(24, H - 132, 156, H - 132)

        self.c.setFont("Helvetica", 10)
        self.c.drawString(24, H - 150, "报价：3万元/天")
        self.c.drawString(24, H - 164, "结算价：2.5万元/天")

        # Right meta panel
        self.c.setFillColor(LIGHT_BLUE)
        self.c.rect(180, H - 180, W - 180, 180, fill=1, stroke=0)

        # Stats
        stats = [
            ("7年", "百家讲坛主讲"),
            ("200+", "期节目播出"),
            ("16+", "可讲主题"),
            ("5本", "专著出版"),
        ]
        x_start = 200
        for i, (val, label) in enumerate(stats):
            x = x_start + i * ((W - 220) / 4)
            self.c.setFillColor(DARK_BLUE)
            self.c.setFont("Helvetica-Bold", 20)
            self.c.drawString(x, H - 80, val)
            self.c.setFillColor(MID_TEXT)
            self.c.setFont("Helvetica", 9)
            self.c.drawString(x, H - 96, label)

        # Meta info on right
        meta_y = H - 118
        meta_items = [
            ("驻地", "厦门（厦大）"),
            ("科研领域", "中国哲学、伦理学、商业伦理、国学"),
        ]
        for label, val in meta_items:
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(DARK_BLUE)
            self.c.drawString(200, meta_y, label + "：")
            self.c.setFont("Helvetica", 9)
            self.c.setFillColor(DARK_TEXT)
            self.c.drawString(200 + 60, meta_y, val)
            meta_y -= 16

        # Divider
        self.c.setStrokeColor(DARK_BLUE)
        self.c.setLineWidth(1.5)
        self.c.line(200, meta_y - 4, W - 24, meta_y - 4)

        #百家讲坛标签
        self.c.setFillColor(ACCENT)
        self.c.roundRect(200, meta_y - 32, 160, 22, 4, fill=1, stroke=0)
        self.c.setFillColor(WHITE)
        self.c.setFont("Helvetica-Bold", 9)
        self.c.drawString(210, meta_y - 24, "⭐ 央视《百家讲坛》常驻嘉宾")

    def draw_section(self, title, y, content_lines):
        """Draw a section with title and bullet lines"""
        # Section title
        self.c.setFillColor(DARK_BLUE)
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(24, y, title)
        # Underline
        self.c.setStrokeColor(DARK_BLUE)
        self.c.setLineWidth(1.5)
        self.c.line(24, y - 4, 200, y - 4)
        return y - 16

    def draw(self):
        self.draw_header()

        # --- 学术背景 ---
        y = H - 210
        y = self.draw_section("学术背景", y)

        bio = (
            "哲学博士，厦门大学管理学院MBA中心教授，博士生导师。主要担任中国哲学、伦理学、美学、"
            "中国文化、商业伦理与企业社会责任、中国管理哲学等课程的教学工作。自2014年3月至2021年11月，"
            "在中央电视台科技频道《百家讲坛》栏目，主讲《大明疑案》《国宝迷踪》等系列节目二百多期，"
            "节目影响力广泛。近年来出版《大明疑案》《国宝迷踪》《晚明风云》《辉煌与悲情》等著作及译著《苏格拉底申辩》。"
        )

        # Word wrap the bio
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(DARK_TEXT)
        from reportlab.lib.utils import simpleSplit
        lines = simpleSplit(bio, "Helvetica", 9, W - 48)
        for line in lines:
            if y < 80:
                self.c.showPage()
                y = H - 40
            self.c.drawString(24, y, line)
            y -= 13
        y -= 8

        # --- 研究领域 ---
        if y < 120:
            self.c.showPage()
            y = H - 40

        y = self.draw_section("研究领域", y)

        tags = ["中国哲学", "伦理学", "美学", "中国文化", "商业伦理",
                "企业社会责任", "国学经典", "阳明心学", "领导力"]
        tag_x = 24
        tag_y = y - 4
        from reportlab.pdfbase.pdfmetrics import stringWidth
        for tag in tags:
            tw = stringWidth(tag, "Helvetica", 9) + 16
            if tag_x + tw > W - 24:
                tag_x = 24
                tag_y -= 22
            self.c.setFillColor(LIGHT_BLUE)
            self.c.roundRect(tag_x, tag_y - 14, tw - 4, 18, 4, fill=1, stroke=0)
            self.c.setFillColor(DARK_BLUE)
            self.c.setFont("Helvetica", 9)
            self.c.drawString(tag_x + 6, tag_y - 8, tag)
            tag_x += tw

        y = tag_y - 24

        # --- 可讲授课程 ---
        if y < 80:
            self.c.showPage()
            y = H - 40

        y = self.draw_section("可讲授课程", y)

        courses = [
            "哲学与人生", "思辨与生活", "孔子与苏格拉底", "爱智·求知·批判——西方哲学思想的演变与现状",
            "传统文化中的管理哲学", "《孙子兵法》中的谋略与智慧", "《周易》的人生智慧", "《周易》的管理哲学",
            "国学智慧与领导艺术", "阳明心学与领导力提升", "辉煌与悲情——两宋史话", "禅的智慧",
            "教育之道——中国传统教育哲学初探", "中国古代艺术文化", "服饰文化与民族精神", "海商与倭寇",
        ]

        col1 = courses[:8]
        col2 = courses[8:]

        col_x = [24, W / 2 + 6]
        for col_idx, col in enumerate([col1, col2]):
            cx = col_x[col_idx]
            cy = y
            for course in col:
                if cy < 80:
                    self.c.showPage()
                    cy = H - 40
                # Bullet
                self.c.setFillColor(DARK_BLUE)
                self.c.circle(cx + 5, cy - 3, 2.5, fill=1, stroke=0)
                self.c.setFillColor(DARK_TEXT)
                self.c.setFont("Helvetica", 8.5)
                lines = simpleSplit(course, "Helvetica", 8.5, W / 2 - 40)
                for i, line in enumerate(lines):
                    self.c.drawString(cx + 14, cy - (i * 12), line)
                    cy -= 12
                cy -= 4

        # Footer
        self.c.setFillColor(LIGHT_TEXT)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(24, 20, "本资料由师资顾问部整理 · 2026年4月 · 如有更新恕不另行通知")

        self.c.save()
        print(f"PDF saved to {self.path}")

pdf = OnePagerPDF("/workspace/fuxiaofan.pdf")
pdf.draw()
