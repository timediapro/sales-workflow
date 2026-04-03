#!/usr/bin/env python3
"""Generate a professional .docx for 傅小凡 without any external dependencies."""
import zipfile, io, os, re
from datetime import datetime

# ── helpers ──────────────────────────────────────────────────────────────────
def xml_esc(s):
    return (s or '').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def para(text, style=None, bold=False, color=None, size=None, space_before=0, space_after=120):
    sz = size or 24  # half-points, 24 = 12pt
    rpr = f'<w:rPr><w:rFonts w:eastAsia="宋体" w:ascii="宋体" w:hAnsi="宋体"/><w:sz w:val="{sz}"/>'
    if bold: rpr += '<w:b/>'
    if color: rpr += f'<w:color w:val="{color}"/>'
    rpr += '</w:rPr>'
    ppr = f'<w:pPr><w:spacing w:before="{space_before}" w:after="{space_after}"/></w:pPr>'
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{xml_esc(text)}</w:t></w:r></w:p>'

def heading(text, color='2C4A7C', space_before=240, space_after=120):
    sz = 32  # 16pt
    ppr = f'<w:pPr><w:pStyle w:val="Heading2"/><w:spacing w:before="{space_before}" w:after="{space_after}"/></w:pPr>'
    rpr = f'<w:rPr><w:rFonts w:eastAsia="黑体" w:ascii="黑体" w:hAnsi="黑体"/><w:b/><w:color w:val="{color}"/><w:sz w:val="{sz}"/></w:rPr>'
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{xml_esc(text)}</w:t></w:r></w:p>'

def bullet(text):
    ppr = '<w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:ind w:left="420" w:hanging="210"/></w:pPr>'
    rpr = '<w:rPr><w:rFonts w:eastAsia="宋体" w:ascii="宋体" w:hAnsi="宋体"/><w:sz w:val="20"/></w:rPr>'
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{xml_esc(text)}</w:t></w:r></w:p>'

def divider():
    return '<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="2C4A7C"/></w:pBdr><w:spacing w:before="0" w:after="60"/></w:pPr></w:p>'

def info_row(label, value):
    return para(f'{label}：{value}', bold=False, size=21, space_before=60, space_after=60)

def callout(text):
    ppr = '<w:pPr><w:pBdr><w:left w:val="single" w:sz="12" w:space="8" w:color="E8A020"/></w:pBdr><w:shd w:val="clear" w:color="auto" w:fill="FFF8E7"/><w:spacing w:before="120" w:after="120"/></w:pPr>'
    rpr = '<w:rPr><w:rFonts w:eastAsia="宋体" w:ascii="宋体" w:hAnsi="宋体"/><w:color w:val="5A4020"/><w:sz w:val="21"/></w:rPr>'
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">⭐ {xml_esc(text)}</w:t></w:r></w:p>'

# ── build document.xml ─────────────────────────────────────────────────────────
def build_body():
    items = []
    # Title
    items.append(para('傅小凡', bold=True, size=56, color='2C4A7C', space_before=0, space_after=60))
    items.append(para('厦门大学管理学院 MBA中心 · 教授 · 博士生导师', size=24, color='444444', space_before=0, space_after=240))
    items.append(divider())

    # 基本信息
    items.append(heading('📋 基本信息'))
    items.append(info_row('驻地', '厦门（厦大）'))
    items.append(info_row('报价', '3万元 / 天'))
    items.append(info_row('结算价', '2.5万元 / 天'))
    items.append(divider())

    # 数据亮点
    items.append(heading('📊 关键数据'))
    stats = [
        '7年  央视《百家讲坛》主讲经验',
        '200+ 期 节目播出',
        '16+  可讲授课程主题',
        '5本  个人专著出版',
    ]
    for s in stats:
        items.append(bullet(s))
    items.append(divider())

    # 学术背景
    items.append(heading('🎓 学术背景'))
    items.append(para(
        '哲学博士，厦门大学管理学院MBA中心教授，博士生导师。主要担任中国哲学、伦理学、美学、中国文化、'
        '商业伦理与企业社会责任、中国管理哲学等课程的教学工作。自2014年3月至2021年11月，在中央电视'
        '台科技频道《百家讲坛》栏目，主讲《大明疑案》《国宝迷踪》等系列节目二百多期，影响力广泛。近年'
        '来出版《大明疑案》《国宝迷踪》《晚明风云》《辉煌与悲情》等著作及译著《苏格拉底申辩》。',
        size=21, space_before=0, space_after=180))
    items.append(callout('央视《百家讲坛》常驻嘉宾，公众知名度高，适合高端论坛、企业内训、政府讲座等场景。'))
    items.append(divider())

    # 研究领域
    items.append(heading('🔬 研究领域'))
    tags = ['中国哲学', '伦理学', '美学', '中国文化', '商业伦理',
            '企业社会责任', '国学经典', '阳明心学', '领导力']
    items.append(para('　'.join(tags), size=21, space_before=0, space_after=180))
    items.append(divider())

    # 可讲授课程
    items.append(heading('📚 可讲授课程（16个主题）'))
    courses = [
        '哲学与人生',
        '思辨与生活',
        '孔子与苏格拉底',
        '爱智·求知·批判——西方哲学思想的演变与现状',
        '传统文化中的管理哲学',
        '《孙子兵法》中的谋略与智慧',
        '《周易》的人生智慧',
        '《周易》的管理哲学',
        '国学智慧与领导艺术',
        '阳明心学与领导力提升',
        '辉煌与悲情——两宋史话',
        '禅的智慧',
        '教育之道——中国传统教育哲学初探',
        '中国古代艺术文化（造型/实用/文学艺术）',
        '服饰文化与民族精神',
        '海商与倭寇',
    ]
    for c in courses:
        items.append(bullet(c))

    items.append(divider())
    items.append(para(f'本资料由师资顾问部整理 · 2026年4月 · 如有更新恕不另行通知',
                      size=18, color='999999', space_before=240, space_after=0))
    return '\n'.join(items)

def build_document_xml():
    body = build_body()
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
            xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
    {body}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1800" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>'''

# ── numbering.xml ─────────────────────────────────────────────────────────────
NUMBERING_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/>
      <w:pPr><w:ind w:left="420" w:hanging="210"/></w:pPr>
      <w:rPr><w:rFonts w:ascii="宋体" w:hAnsi="宋体" w:eastAsia="宋体" w:hint="eastAsia"/></w:rPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>'''

# ── styles.xml ────────────────────────────────────────────────────────────────
STYLES_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault><w:rPr>
      <w:rFonts w:eastAsia="宋体" w:ascii="宋体" w:hAnsi="宋体" w:hint="eastAsia"/>
      <w:sz w:val="24"/><w:szCs w:val="24"/>
    </w:rPr></w:rPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:styleId="Normal" w:default="1">
    <w:name w:val="Normal"/>
    <w:rPr><w:rFonts w:eastAsia="宋体" w:ascii="宋体" w:hAnsi="宋体"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr>
    <w:rPr><w:rFonts w:eastAsia="黑体" w:ascii="黑体" w:hAnsi="黑体"/><w:b/><w:color w:val="2C4A7C"/><w:sz w:val="32"/></w:rPr>
  </w:style>
</w:styles>'''

# ── relationships ──────────────────────────────────────────────────────────────
RELS_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''

# ── [Content_Types].xml ───────────────────────────────────────────────────────
CT_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>'''

TOPLEVEL_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

# ── write .docx ───────────────────────────────────────────────────────────────
OUT = '/workspace/fuxiaofan.docx'
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', CT_XML)
    z.writestr('_rels/.rels', TOPLEVEL_RELS)
    z.writestr('word/document.xml', build_document_xml())
    z.writestr('word/styles.xml', STYLES_XML)
    z.writestr('word/numbering.xml', NUMBERING_XML)
    z.writestr('word/_rels/document.xml.rels', RELS_XML)

size = os.path.getsize(OUT)
print(f'DOCX written → {OUT}  ({size:,} bytes)')
