#The python program code for LAB TECHNICIAN ASSISTANT v7.2 :

# -*- coding: utf-8 -*-
"""
═════════════════════════════════════════════════════════════
══════
        Lab Technician Assistant v7.2 — Unified Multilingual Edition

  Developed in collaboration between:
    • Mohammad.A.M.Mousa (Abdel Qader) — Laboratory Technician
    • DeepSeek AI — Code assistance & architecture review

  Built with Python 3 + CustomTkinter
  Distributed as a standalone Windows executable (.exe)
  Works offline — no Python installation required after publishing

  License: MIT  |  Year: 2025
═════════════════════════════════════════════════════════════
══════
"""
import customtkinter as ctk
from tkinter import messagebox, filedialog
import math, statistics, re, csv
from datetime import datetime

# ═══════════════════════════════════════════════════
#                  ةمجرتلا (AR/EN/DE)
# ═══════════════════════════════════════════════════
LANG = "ar"

T = {
"ar": {
"title":'مساعد فني المختبرات       ',"lab":'مختبر',
"home":'الرئيسية        ',"sol":'تحضير المحاليل         ',"dil":'التخفيف  ',
"ph":'      pH والأحماض',"buf":'المحاليل المنظمة        ',"mw":'الوزن الجزيئي         ',
"stat":'اإلحصاء       ',"val":'Validation التحقق      ',"phy":'الفيزياء      ',
"unt":'تحويل الوحدات    ',"hist":'السجل         ',
"theme":'المظهر    /  ',"lang":'اللغة   ',
"calc":'احسب',"clear":'مسح  🗑',"export":'CSV تصدير       ',
"refresh":'تحديث    ',"clr_hist":'مسح السجل 🗑',
"error":'خطأ ',"info":'تنبيه',"done":'تم',"confirm":'تأكيد ',
"welcome":'مرحبًا بك في مساعد فني المختبرات',
"sub":'تطوير مشترك: Mohammad.A.M.Mousa (Abdel Qader) × DeepSeek AI | Python 3 | مستقل كملف تنفيذي',
"f_sol":'تحضير المحاليل',"f_sol_d":'مولارية · معيارية · % · ppm',
"f_dil":'التخفيف',"f_dil_d":"C₁V₁ = C₂V₂",
"f_ph":'pH والأحماض',"f_ph_d":'Ka · Kb · قوي/ضعيف',
"f_buf":'المحاليل المنظمة',"f_buf_d":"Henderson-Hasselbalch",
"f_mw":'الوزن الجزيئي',"f_mw_d":'من الصيغة (هيدرات)',
"f_stat":'اإلحصاء',"f_stat_d":'SD · CV · CI 95% · متوسط',
"f_val":'التحقق',"f_val_d":'ANOVA · خطية · دقة · ضبط',
"f_phy":'الفيزياء',"f_phy_d":'Beer-Lambert · كثافة · غاز',
"f_unt":'الوحدات ',"f_unt_d":'حجم · كتلة · حرارة · ضغط',
"mode_m":'المولارية M',"mode_mm":'المولالية m',
"mode_n":'العيارية N',"mode_p":"% w/v","mode_ppm":"ppm",
"lbl_mw":'الوزن الجزيئي (g/mol)',"lbl_v":'الحجم (mL)',
"lbl_c":'التركيز',"lbl_eq":'عدد المكافئات',
"ph_mw":'مثال: 58.44',"ph_v":'مثال: 500',
"ph_c":'مثال: 0.5',"ph_eq":'مثال: 2',
"c1":"C₁","v1":"V₁ (mL)","c2":"C₂","v2":"V₂ (mL)",
"ph_c1":'مثال: 1',"ph_v1":'مثال: 50',"ph_c2":'مثال: 0.1',
"ph_v2":'اتركه فارغًا',
"strong_a":'حمض قوي',"weak_a":'حمض ضعيف',
"strong_b":'قاعدة قوية',"weak_b":'قاعدة ضعيفة',
"lbl_conc":'التركيز (M)',"lbl_ka":'Ka أو Kb',
"ph_conc":'مثال: 0.1',"ph_ka":'مثال: 1.8e-5',
"lbl_pka":"pKa","lbl_ph":'pH المطلوب',"lbl_ct":'التركيز الكلي (M)',
"ph_pka":'مثال: 4.76',"ph_ph":'مثال: 5.0',
"lbl_formula":'الصيغة الكيميائية',"ph_formula":'مثال: H2SO4',
"ex":'أمثلة:',
"stat_note":'أدخل أرقامًا مفصولة بفواصل',
"v_lin":'الخطية     ',"v_acc":'الدقة        ',"v_prec":'الضبط      ',
"v_lod":"    LOD/LOQ","v_sys":'ملاءمة النظام    ',"v_anova":"       ANOVA",
"v_conc":'التراكيز (مفصولة بفاصلة)',
"v_area":'المساحات (مفصولة بفاصلة)',
"v_calc_lin":'احسب الخطية',"v_slope":'الميل ',"v_int":'التقاطع',
"v_r2":"R²","v_eq":'المعادلة ',"v_ok":'مطابق (R² ≥ 0.995)',
"v_no":'غير مطابق (R² < 0.995)',
"v_exp":'القيمة المتوقعة',"v_meas":'القيمة المقاسة',
"v_calc_rec":'احسب الاسترداد',"v_rec":'الاسترداد %',
"v_rec_ok":'مطابق (98-102%)',"v_rec_no":'خارج المدى',
"v_values":'القيم (مفصولة بفاصلة)',"v_calc_pr":'احسب الضبط',
"v_mean":'المتوسط',"v_sd":"SD","v_rsd":"RSD %",
"v_pr_ok":'مطابق (RSD ≤ 2%)',"v_pr_no":'أعلى من الحد',
"v_sigma":"σ (SD)","v_slope_s":'S (الميل)',
"v_calc_lod":'احسب LOD/LOQ',"v_lod_r":"LOD","v_loq_r":"LOQ",
"v_tR":"tR (min)","v_W":"W (min)","v_calc_N":'احسب N',
"v_N":'عدد الأطباق N',"v_N_ok":'مطابق (N>2000)',
"v_N_no":"    < 2000",
"v_tR1":"tR₁","v_tR2":"tR₂","v_W1":"W₁","v_W2":"W₂",
"v_calc_Rs":'احسب Rs',"v_Rs":'دقة الفصل Rs',
"v_Rs_ok":'مطابق (Rs>1.5)',"v_Rs_no":"    < 1.5",
"v_groups":'كل مجموعة في سطر (قيم مفصولة بفواصل)',
"v_calc_anova":'احسب ANOVA',"v_ssb":'SS بين',"v_ssw":'SS داخل',
"v_msb":"MSB","v_msw":"MSW","v_f":'F محسوبة',"v_fc":'F  حرجة',
"v_sig":'فرق معنوي (F > F_crit)',
"v_nosig":'لا يوجد فرق معنوي (F ≤ F_crit)',
"p_dens":'الكثافة',"p_gas":'الغاز المثالي',
"p_beer":"Beer-Lambert","p_stock":'تحضير من مخزون',
"lbl_mass":'الكتلة (g)',"lbl_vol":'الحجم (mL)',
"ph_mass":'مثال: 25',"ph_vol":'مثال: 10',
"note_empty":'اترك الحقل المطلوب فارغًا',
"u_vol":'الحجم ',"u_mass":'الكتلة ',"u_pres":'الضغط',
"u_temp":'الحرارة',"u_conc":'التركيز',
"u_from":'من:',"u_val":'القيمة:',"u_unit":'الوحدة:',
"u_conv":'تحويل ↔',"u_temp_note":'تحويل درجات الحرارة',
"u_conc_note":'املأ MW + قيمة واحدة',
"u_conv_temp":'حوّل',"u_conv_conc":'حوّل',
"no_hist":'لا يوجد سجل',
"exported":'تم تصدير {n} سجل',
"clr_q":'مسح السجل بالكامل؟',
"check_inputs":'تحقق من المدخلات',
"save_ok":'تم الحفظ ',
"choose":'اختر ملفًا',
"cat_sol":'تحضير محلول',"cat_dil":'تخفيف',"cat_ph":"pH",
"cat_buf":'محلول منظم',"cat_mw":'وزن جزيئي',"cat_stat":'إحصاء',
"cat_val":'تحقق',"cat_dens":'كثافة',"cat_gas":'غاز',
"cat_beer":"Beer-Lambert","cat_stock":'من مخزون',
"cat_conv":'تحويل',"cat_temp":'حرارة ',"cat_conc":'تركيز',
},

"en": {
"title":"      Lab Technician Assistant","lab":"Lab",
"home":"        Home","sol":"         Solutions","dil":"  Dilution",
"ph":"      pH & Acids","buf":"        Buffers","mw":"         Mol. Weight",
"stat":"      Statistics","val":"      Validation","phy":"      Physics",
"unt":"    Units","hist":"         History",
"theme":"  /   Theme","lang":"  Language",
"calc":"Calculate","clear":"🗑 Clear","export":"       Export CSV",
"refresh":"    Refresh","clr_hist":"🗑 Clear History",
"error":"Error","info":"Info","done":"Done","confirm":"Confirm",
"welcome":"Welcome to Lab Technician Assistant",
"sub":"By Mohammad.A.M.Mousa (Abdel Qader) in collaboration with DeepSeek AI | Python 3 | Standalone executable",
"f_sol":"Solution Prep","f_sol_d":"Molarity · Normality · % · ppm",
"f_dil":"Dilution","f_dil_d":"C₁V₁ = C₂V₂",
"f_ph":"pH & Acids","f_ph_d":"Strong/Weak · Ka · Kb",
"f_buf":"Buffers","f_buf_d":"Henderson-Hasselbalch",
"f_mw":"Mol. Weight","f_mw_d":"From formula (hydrates)",
"f_stat":"Statistics","f_stat_d":"Mean · SD · CV · CI 95%",
"f_val":"Validation","f_val_d":"Linearity · Accuracy · ANOVA",
"f_phy":"Physics","f_phy_d":"Density · Gas · Beer-Lambert",
"f_unt":"Units","f_unt_d":"Volume · Mass · Temp · Pressure",
"mode_m":"Molarity M","mode_mm":"Molality m",
"mode_n":"Normality N","mode_p":"% w/v","mode_ppm":"ppm",
"lbl_mw":"Molecular Weight (g/mol)","lbl_v":"Volume (mL)",
"lbl_c":"Concentration","lbl_eq":"Equivalents",
"ph_mw":"e.g. 58.44","ph_v":"e.g. 500","ph_c":"e.g. 0.5",
"ph_eq":"e.g. 2",
"c1":"C₁","v1":"V₁ (mL)","c2":"C₂","v2":"V₂ (mL)",
"ph_c1":"e.g. 1","ph_v1":"e.g. 50","ph_c2":"e.g. 0.1",
"ph_v2":"Leave empty",
"strong_a":"Strong Acid","weak_a":"Weak Acid",
"strong_b":"Strong Base","weak_b":"Weak Base",
"lbl_conc":"Concentration (M)","lbl_ka":"Ka or Kb",
"ph_conc":"e.g. 0.1","ph_ka":"e.g. 1.8e-5",
"lbl_pka":"pKa","lbl_ph":"Target pH","lbl_ct":"Total Conc. (M)",
"ph_pka":"e.g. 4.76","ph_ph":"e.g. 5.0",
"lbl_formula":"Chemical Formula","ph_formula":"e.g. H2SO4",
"ex":"Examples:",
"stat_note":"Enter numbers separated by commas",
"v_lin":"    Linearity","v_acc":"       Accuracy","v_prec":"      Precision",
"v_lod":"    LOD/LOQ","v_sys":"    System Suitability","v_anova":"       ANOVA",
"v_conc":"Concentrations (comma-separated)",
"v_area":"Areas (comma-separated)",
"v_calc_lin":"Calculate Linearity","v_slope":"Slope","v_int":"Intercept",
"v_r2":"R²","v_eq":"Equation","v_ok":"   Compliant (R² ≥ 0.995)",
"v_no":"  Not Compliant (R² < 0.995)",
"v_exp":"Expected Value","v_meas":"Measured Value",
"v_calc_rec":"Calculate Recovery","v_rec":"Recovery %",
"v_rec_ok":"   Compliant (98-102%)","v_rec_no":"    Out of range",
"v_values":"Values (comma-separated)","v_calc_pr":"Calculate Precision",
"v_mean":"Mean","v_sd":"SD","v_rsd":"RSD %",
"v_pr_ok":"   Compliant (RSD ≤ 2%)","v_pr_no":"    Above limit",
"v_sigma":"σ (SD)","v_slope_s":"S (Slope)",
"v_calc_lod":"Calculate LOD/LOQ","v_lod_r":"LOD","v_loq_r":"LOQ",
"v_tR":"tR (min)","v_W":"W (min)","v_calc_N":"Calculate N",
"v_N":"Theoretical Plates N","v_N_ok":"   Compliant (N>2000)",
"v_N_no":"    < 2000",
"v_tR1":"tR₁","v_tR2":"tR₂","v_W1":"W₁","v_W2":"W₂",
"v_calc_Rs":"Calculate Rs","v_Rs":"Resolution Rs",
"v_Rs_ok":"   Compliant (Rs>1.5)","v_Rs_no":"    < 1.5",
"v_groups":"One group per line (comma-separated)",
"v_calc_anova":"Calculate ANOVA","v_ssb":"SS Between","v_ssw":"SS Within",
"v_msb":"MSB","v_msw":"MSW","v_f":"F calculated","v_fc":"F critical",
"v_sig":"    Significant difference (F > F_crit)",
"v_nosig":"   No significant difference (F ≤ F_crit)",
"p_dens":"Density","p_gas":"Ideal Gas",
"p_beer":"Beer-Lambert","p_stock":"From Stock",
"lbl_mass":"Mass (g)","lbl_vol":"Volume (mL)",
"ph_mass":"e.g. 25","ph_vol":"e.g. 10",
"note_empty":"Leave the field to compute empty",
"u_vol":"Volume","u_mass":"Mass","u_pres":"Pressure",
"u_temp":"Temperature","u_conc":"Concentration",
"u_from":"From:","u_val":"Value:","u_unit":"Unit:",
"u_conv":"↔ Convert","u_temp_note":"Temperature Conversion",
"u_conc_note":"Fill MW + one value",
"u_conv_temp":"     Convert","u_conv_conc":"    Convert",
"no_hist":"No history",
"exported":"Exported {n} records",
"clr_q":"Clear entire history?",
"check_inputs":"Check inputs",
"save_ok":"Saved",
"choose":"Choose file",
"cat_sol":"Solution","cat_dil":"Dilution","cat_ph":"pH",
"cat_buf":"Buffer","cat_mw":"Mol. Weight","cat_stat":"Stats",
"cat_val":"Validation","cat_dens":"Density","cat_gas":"Gas",
"cat_beer":"Beer-Lambert","cat_stock":"From Stock",
"cat_conv":"Convert","cat_temp":"Temp","cat_conc":"Concentration",
},

"de": {
"title":"      Labortechniker-Assistent","lab":"Labor",
"home":"        Startseite","sol":"         Lösungen","dil":"  Verdünnung",
"ph":"      pH & Säuren","buf":"        Puffer","mw":"         Molmasse",
"stat":"      Statistik","val":"      Validierung","phy":"      Physik",
"unt":"    Einheiten","hist":"         Verlauf",
"theme":"  /   Design","lang":"  Sprache",
"calc":"Berechnen","clear":"🗑 Löschen","export":"       CSV export",
"refresh":"    Aktualisieren","clr_hist":"🗑 Verlauf löschen",
"error":"Fehler","info":"Info","done":"Fertig","confirm":"Bestätigen",
"welcome":"Willkommen beim Labortechniker-Assistenten",
"sub":"Von Mohammad.A.M.Mousa (Abdel Qader) mit DeepSeek AI | Python 3 | Eigenständige .exe",
"f_sol":"Lösungen","f_sol_d":"Molarität · Normalität · % · ppm",
"f_dil":"Verdünnung","f_dil_d":"C₁V₁ = C₂V₂",
"f_ph":"pH & Säuren","f_ph_d":"Stark/Schwach · Ka · Kb",
"f_buf":"Puffer","f_buf_d":"Henderson-Hasselbalch",
"f_mw":"Molmasse","f_mw_d":"Aus Formel (Hydrate)",
"f_stat":"Statistik","f_stat_d":"MW · SD · CV · KI 95%",
"f_val":"Validierung","f_val_d":"Linearität · Genauigkeit · ANOVA",
"f_phy":"Physik","f_phy_d":"Dichte · Gas · Beer-Lambert",
"f_unt":"Einheiten","f_unt_d":"Volumen · Masse · Temp · Druck",
"mode_m":"Molarität M","mode_mm":"Molalität m",
"mode_n":"Normalität N","mode_p":"% w/v","mode_ppm":"ppm",
"lbl_mw":"Molmasse (g/mol)","lbl_v":"Volumen (mL)",
"lbl_c":"Konzentration","lbl_eq":"Äquivalente",
"ph_mw":"z.B. 58.44","ph_v":"z.B. 500","ph_c":"z.B. 0.5",
"ph_eq":"z.B. 2",
"c1":"C₁","v1":"V₁ (mL)","c2":"C₂","v2":"V₂ (mL)",
"ph_c1":"z.B. 1","ph_v1":"z.B. 50","ph_c2":"z.B. 0.1",
"ph_v2":"Leer lassen",
"strong_a":"Starke Säure","weak_a":"Schwache Säure",
"strong_b":"Starke Base","weak_b":"Schwache Base",
"lbl_conc":"Konzentration (M)","lbl_ka":"Ka oder Kb",
"ph_conc":"z.B. 0.1","ph_ka":"z.B. 1.8e-5",
"lbl_pka":"pKa","lbl_ph":"Ziel-pH","lbl_ct":"Gesamtkonz. (M)",
"ph_pka":"z.B. 4.76","ph_ph":"z.B. 5.0",
"lbl_formula":"Chemische Formel","ph_formula":"z.B. H2SO4",
"ex":"Beispiele:",
"stat_note":"Zahlen durch Kommas getrennt",
"v_lin":"    Linearität","v_acc":"       Genauigkeit","v_prec":"      Präzision",
"v_lod":"    LOD/LOQ","v_sys":"    Systemeignung","v_anova":"       ANOVA",
"v_conc":"Konzentrationen (Komma)",
"v_area":"Flächen (Komma)",
"v_calc_lin":"Linearität","v_slope":"Steigung","v_int":"Achsenabschnitt",
"v_r2":"R²","v_eq":"Gleichung","v_ok":"   Konform (R² ≥ 0.995)",
"v_no":"  Nicht konform (R² < 0.995)",
"v_exp":"Erwarteter Wert","v_meas":"Gemessener Wert",
"v_calc_rec":"Wiederfindung","v_rec":"Wiederfindung %",
"v_rec_ok":"   Konform (98-102%)","v_rec_no":"    Außerhalb",
"v_values":"Werte (Komma)","v_calc_pr":"Präzision",
"v_mean":"Mittelwert","v_sd":"SD","v_rsd":"RSD %",
"v_pr_ok":"   Konform (RSD ≤ 2%)","v_pr_no":"    Über Grenze",
"v_sigma":"σ (SD)","v_slope_s":"S (Steigung)",
"v_calc_lod":"LOD/LOQ","v_lod_r":"LOD","v_loq_r":"LOQ",
"v_tR":"tR (min)","v_W":"W (min)","v_calc_N":"N berechnen",
"v_N":"Böden N","v_N_ok":"   Konform (N>2000)",
"v_N_no":"    < 2000",
"v_tR1":"tR₁","v_tR2":"tR₂","v_W1":"W₁","v_W2":"W₂",
"v_calc_Rs":"Rs berechnen","v_Rs":"Auflösung Rs",
"v_Rs_ok":"   Konform (Rs>1.5)","v_Rs_no":"    < 1.5",
"v_groups":"Eine Gruppe pro Zeile",
"v_calc_anova":"ANOVA","v_ssb":"SS zwischen","v_ssw":"SS innerhalb",
"v_msb":"MSB","v_msw":"MSW","v_f":"F berechnet","v_fc":"F kritisch",
"v_sig":"    Signifikanter Unterschied",
"v_nosig":"   Kein signifikanter Unterschied",
"p_dens":"Dichte","p_gas":"Ideales Gas",
"p_beer":"Beer-Lambert","p_stock":"Aus Stammlösung",
"lbl_mass":"Masse (g)","lbl_vol":"Volumen (mL)",
"ph_mass":"z.B. 25","ph_vol":"z.B. 10",
"note_empty":"Zu berechnendes Feld leer lassen",
"u_vol":"Volumen","u_mass":"Masse","u_pres":"Druck",
"u_temp":"Temperatur","u_conc":"Konzentration",
"u_from":"Von:","u_val":"Wert:","u_unit":"Einheit:",
"u_conv":"↔ Umrechnen","u_temp_note":"Temperaturumrechnung",
"u_conc_note":"MW + einen Wert",
"u_conv_temp":"     Umrechnen","u_conv_conc":"    Umrechnen",
"no_hist":"Kein Verlauf",
"exported":"{n} Einträge exportiert",
"clr_q":"Verlauf löschen?",
"check_inputs":"Eingaben prüfen",
"save_ok":"Gespeichert",
"choose":"Datei wählen",
"cat_sol":"Lösung","cat_dil":"Verdünnung","cat_ph":"pH",
"cat_buf":"Puffer","cat_mw":"Molmasse","cat_stat":"Statistik",
"cat_val":"Validierung","cat_dens":"Dichte","cat_gas":"Gas",
"cat_beer":"Beer-Lambert","cat_stock":"Stammlösung",
"cat_conv":"Umrechnung","cat_temp":"Temperatur","cat_conc":"Konzentration",
},
}

def tr(k, **kw):
    s = T.get(LANG, T["ar"]).get(k, k)
    if kw:
        try: return s.format(**kw)
        except: return s
    return s

def rtl(): return LANG == "ar"
def anc(): return "e" if rtl() else "w"
def jst(): return "right" if rtl() else "left"
def sd(): return "right" if rtl() else "left"

# ═══════════════════════════════════════════════════
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

AM = {'H':1.008,'He':4.0026,'Li':6.94,'Be':9.0122,'B':10.81,'C':12.011,
'N':14.007,'O':15.999,'F':18.998,'Ne':20.18,'Na':22.99,'Mg':24.305,
'Al':26.982,'Si':28.085,'P':30.974,'S':32.06,'Cl':35.45,'Ar':39.948,
'K':39.098,'Ca':40.078,'Sc':44.956,'Ti':47.867,'V':50.942,'Cr':51.996,
'Mn':54.938,'Fe':55.845,'Co':58.933,'Ni':58.693,'Cu':63.546,'Zn':65.38,
'Ga':69.723,'Ge':72.63,'As':74.922,'Se':78.971,'Br':79.904,'Kr':83.798,
'Rb':85.468,'Sr':87.62,'Y':88.906,'Zr':91.224,'Nb':92.906,'Mo':95.95,
'Ag':107.87,'Cd':112.41,'In':114.82,'Sn':118.71,'Sb':121.76,'I':126.9,
'Ba':137.33,'Pt':195.08,'Au':196.97,'Hg':200.59,'Pb':207.2,'U':238.03}

def ff(s):
    s = str(s).strip().replace(',', '.')
    if not s: raise ValueError("Empty")
    return float(s)

def _pg(f):
    t, i = 0.0, 0
    while i < len(f):
        c = f[i]
        if c == '(':
            d, j = 1, i+1
            while j < len(f) and d > 0:
                if f[j]=='(': d+=1
                elif f[j]==')': d-=1
                j+=1
            inner = f[i+1:j-1]
            k, nm = j, ''
            while k < len(f) and f[k].isdigit(): nm += f[k]; k += 1
            t += _pg(inner) * (int(nm) if nm else 1); i = k
        elif c.isupper():
            s = c; i += 1
            while i < len(f) and f[i].islower(): s += f[i]; i += 1
            nm = ''
            while i < len(f) and f[i].isdigit(): nm += f[i]; i += 1
            if s not in AM: raise ValueError(f"Unknown: {s}")
            t += AM[s] * (int(nm) if nm else 1)
        else: i += 1
    return t

def pf(f):
    f = f.strip()
    if not f: raise ValueError("Empty")
    ps = re.split(r'[·.*]', f)
    if len(ps) == 1: return _pg(ps[0])
    t = _pg(ps[0])
    for p in ps[1:]:
        m = re.match(r'^(\d+)(.+)$', p)
        t += int(m.group(1)) * _pg(m.group(2)) if m else _pg(p)
    return t

def ce(f):
    c = {}
    def w(s, mu):
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == '(':
                d, j = 1, i+1
                while j < len(s) and d > 0:
                    if s[j]=='(': d+=1
                    elif s[j]==')': d-=1
                    j+=1
                inner = s[i+1:j-1]
                k, nm = j, ''
                while k < len(s) and s[k].isdigit(): nm += s[k]; k += 1
                w(inner, mu * (int(nm) if nm else 1)); i = k
            elif ch.isupper():
                sy = ch; i += 1
                while i < len(s) and s[i].islower(): sy += s[i]; i += 1
                nm = ''
                while i < len(s) and s[i].isdigit(): nm += s[i]; i += 1
                c[sy] = c.get(sy, 0) + (int(nm) if nm else 1) * mu
            else: i += 1
    ps = re.split(r'[·.*]', f)
    if len(ps) == 1: w(ps[0], 1)
    else:
        w(ps[0], 1)
        for p in ps[1:]:
            m = re.match(r'^(\d+)(.+)$', p)
            w(m.group(2), int(m.group(1))) if m else w(p, 1)
    return c

# ═══════════════════════════════════════════════════
class HIST:
    rec = []
    @classmethod
    def add(cls, k, d):
        cls.rec.append({'t': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'k': k, 'd': d})
    @classmethod
    def exp(cls, p):
        with open(p, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f); w.writerow(['Time','Category','Details'])
            for r in cls.rec: w.writerow([r['t'], tr(r['k']), r['d']])

# ═══════════════════════════════════════════════════
class F(ctk.CTkFrame):
    def __init__(self, m, lb, ph="", w=170):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=lb, font=("Tahoma",12), anchor=anc()
                     ).pack(anchor=anc(), pady=(0,3))
        self.e = ctk.CTkEntry(self, width=w, height=34, placeholder_text=ph,
                              font=("Tahoma",12), justify=jst())
        self.e.pack()
    def g(self): return self.e.get()
    def s(self, v): self.e.delete(0,"end"); self.e.insert(0,str(v))
    def c(self): self.e.delete(0,"end")
class RB(ctk.CTkTextbox):
    def __init__(self, m, h=200, **kw):
        super().__init__(m, height=h, font=("Consolas",12),
                         corner_radius=10, wrap="word", **kw)
    def show(self, t): self.delete("1.0","end"); self.insert("1.0",t)
    def clr(self): self.delete("1.0","end")

def mkform(p, data):
    fr = ctk.CTkFrame(p, corner_radius=12, fg_color=("#ebebeb","#1f2025"))
    fr.pack(pady=12, padx=20, fill="x")
    D = {}
    for col,(k,lb,ph,w) in enumerate(data):
        ff_ = F(fr, lb, ph, w)
        ff_.grid(row=0, column=col, padx=12, pady=15)
        D[k] = ff_
    return fr, D

# ═══════════════════════════════════════════════════
class HomeP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("welcome"), font=("Tahoma",26,"bold")
                     ).pack(pady=(30,5))
        ctk.CTkLabel(self, text=tr("sub"), font=("Tahoma",12),
                     text_color=("#666","#aaa"),
                     wraplength=700, justify="center").pack(pady=(0,25))
        g = ctk.CTkFrame(self, fg_color="transparent"); g.pack(pady=10)
        feats = [("        ","f_sol","f_sol_d"),(" ","f_dil","f_dil_d"),
                 ("     ","f_ph","f_ph_d"),("       ","f_buf","f_buf_d"),
                 ("        ","f_mw","f_mw_d"),("     ","f_stat","f_stat_d"),
                 ("     ","f_val","f_val_d"),("     ","f_phy","f_phy_d"),
                 ("   ","f_unt","f_unt_d")]
        for i,(ic,tk_,dk) in enumerate(feats):
            r,c = divmod(i,2)
            cd = ctk.CTkFrame(g, corner_radius=12,
                              fg_color=("#e8f0fe","#252a35"),
                              width=330, height=95)
            cd.grid(row=r, column=c, padx=10, pady=6)
            cd.grid_propagate(False)
            ctk.CTkLabel(cd, text=f"{ic}  {tr(tk_)}",
                         font=("Tahoma",15,"bold"), anchor=anc()
                         ).pack(anchor=anc(), padx=15, pady=(12,5))
            ctk.CTkLabel(cd, text=tr(dk), font=("Tahoma",11),
                         anchor=anc(), text_color=("#555","#bbb"),
                         wraplength=300, justify=jst()
                         ).pack(anchor=anc(), padx=15)

# ═══════════════════════════════════════════════════
class SolP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("sol"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        mr = ctk.CTkFrame(self, fg_color="transparent"); mr.pack(pady=5)
        self.md = ctk.StringVar(value="m")
        for k,v in [("mode_m","m"),("mode_mm","mm"),
                    ("mode_n","n"),("mode_p","p"),("mode_ppm","ppm")]:
            ctk.CTkRadioButton(mr, text=tr(k), variable=self.md, value=v,
                               font=("Tahoma",12), command=self.upd
                               ).pack(side=sd(), padx=8)
        self.fr, self.D = mkform(self, [
            ("mw", tr("lbl_mw"), tr("ph_mw"), 150),
            ("v", tr("lbl_v"), tr("ph_v"), 130),
            ("c", tr("lbl_c"), tr("ph_c"), 130),
            ("eq", tr("lbl_eq"), tr("ph_eq"), 110)])
        b = ctk.CTkFrame(self, fg_color="transparent"); b.pack(pady=8)
        ctk.CTkButton(b, text=tr("calc"), font=("Tahoma",14,"bold"),
                      height=40, width=180, command=self.go
                      ).pack(side=sd(), padx=5)
        ctk.CTkButton(b, text=tr("clear"), font=("Tahoma",13), height=40,
                      width=100, fg_color=("#a55","#803030"),
                      command=self.clr).pack(side=sd(), padx=5)
        self.rb = RB(self, 250)
        self.rb.pack(fill="both", expand=True, padx=20, pady=(5,15))
        self.upd()
    def upd(self):
        if self.md.get()=="n": self.D["eq"].grid()
        else: self.D["eq"].grid_remove()
    def clr(self):
        for f in self.D.values(): f.c()
        self.rb.clr()
    def go(self):
        try:
            mo = self.md.get()
            mw = ff(self.D["mw"].g()); v = ff(self.D["v"].g())
            if mw<=0 or v<=0: raise ValueError("MW/V > 0")
            vL = v/1000; out = []
            if mo=="m":
                c = ff(self.D["c"].g()); mass = c*vL*mw
                out = [f"     Molarity (M)",
                       f"• Mass = {c} × {vL:.4f} × {mw} = {mass:.4f} g",
                       "", "Steps:",
                       f"  1. Weigh {mass:.4f} g",
                       f"  2. Dissolve",
                       f"  3. Dilute to {v:.0f} mL"]
            elif mo=="mm":
                c = ff(self.D["c"].g()); mass = c*vL*mw
                out = [f"     Molality (m)",
                       f"• Mass = {mass:.4f} g"]
            elif mo=="n":
                c = ff(self.D["c"].g()); eq = ff(self.D["eq"].g())
                if eq<=0: raise ValueError("Eq > 0")
                M = c/eq; mass = M*vL*mw
                out = [f"     Normality (N)",
                       f"• M = {c}/{eq} = {M:.4f} M",
                       f"• Mass = {mass:.4f} g"]
            elif mo=="p":
                c = ff(self.D["c"].g()); mass = c*v/100
                out = [f"     % w/v = {c} → Mass = {mass:.4f} g"]
            else:
                c = ff(self.D["c"].g()); mg = c*vL
                out = [f"     ppm = {c} → Mass = {mg:.4f} mg"]
            self.rb.show("\n".join(out))
            HIST.add("cat_sol", out[0])
        except Exception as e:
            messagebox.showerror(tr("error"), f"{tr('check_inputs')}:\n{e}")

# ═══════════════════════════════════════════════════
class DilP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("dil"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        ctk.CTkLabel(self, text="C₁ · V₁ = C₂ · V₂",
                     font=("Tahoma",15,"italic"),
                     text_color=("#1a73e8","#4da3ff")).pack(pady=(0,8))
        self.fr, self.D = mkform(self, [
            ("c1", tr("c1"), tr("ph_c1"), 150),
            ("v1", tr("v1"), tr("ph_v1"), 150),
            ("c2", tr("c2"), tr("ph_c2"), 150),
            ("v2", tr("v2"), tr("ph_v2"), 150)])
        b = ctk.CTkFrame(self, fg_color="transparent"); b.pack(pady=8)
        ctk.CTkButton(b, text=tr("calc"), font=("Tahoma",14,"bold"),
                      height=40, width=180, command=self.go
                      ).pack(side=sd(), padx=5)
        ctk.CTkButton(b, text=tr("clear"), font=("Tahoma",13), height=40,
                      width=100, fg_color=("#a55","#803030"),
                      command=self.clr).pack(side=sd(), padx=5)
        self.rb = RB(self, 270)
        self.rb.pack(fill="both", expand=True, padx=20, pady=(5,15))
    def clr(self):
        for f in self.D.values(): f.c()
        self.rb.clr()
    def go(self):
        try:
            v = {k:f.g().strip() for k,f in self.D.items()}
            emp = [k for k,x in v.items() if not x]
            if len(emp)!=1: raise ValueError(tr("ph_v2"))
            n = {k:ff(x) for k,x in v.items() if x}
            out = []
            if "v2" in emp:
                v2 = n["c1"]*n["v1"]/n["c2"]; add = v2 - n["v1"]
                out = [f"     V₂ = {v2:.4f} mL",
                       f"  Solvent to add = {add:.4f} mL",
                       "", "Steps:",
                       f"  1. Take {n['v1']:.2f} mL of {n['c1']}",
                       f"  2. Add {add:.2f} mL solvent",
                       f"  3. Dilute to {v2:.2f} mL"]
                if add < 0: out.append("    Negative")
            elif "v1" in emp:
                out = [f"     V₁ = {n['c2']*n['v2']/n['c1']:.4f} mL"]
            elif "c1" in emp:
                out = [f"     C₁ = {n['c2']*n['v2']/n['v1']:.4f}"]
            elif "c2" in emp:
                out = [f"     C₂ = {n['c1']*n['v1']/n['v2']:.4f}"]
            self.rb.show("\n".join(out)); HIST.add("cat_dil", out[0])
        except Exception as e:
            messagebox.showerror(tr("error"), f"{tr('check_inputs')}:\n{e}")

# ═══════════════════════════════════════════════════
class PHP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("ph"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        r = ctk.CTkFrame(self, fg_color="transparent"); r.pack(pady=5)
        self.kd = ctk.StringVar(value="sa")
        for k,v in [("strong_a","sa"),("weak_a","wa"),
                    ("strong_b","sb"),("weak_b","wb")]:
            ctk.CTkRadioButton(r, text=tr(k), variable=self.kd, value=v,
                               font=("Tahoma",12), command=self.tog
                               ).pack(side=sd(), padx=8)
        self.fr, self.D = mkform(self, [
            ("c", tr("lbl_conc"), tr("ph_conc"), 180),
            ("k", tr("lbl_ka"), tr("ph_ka"), 180)])
        ctk.CTkButton(self, text=tr("calc"), font=("Tahoma",14,"bold"),
                      height=40, width=200, command=self.go
                      ).pack(pady=10)
        self.rb = RB(self, 270)
        self.rb.pack(fill="both", expand=True, padx=20, pady=(5,15))
        self.tog()
    def tog(self):
        if self.kd.get() in ("wa","wb"): self.D["k"].grid()
        else: self.D["k"].grid_remove()
    def go(self):
        try:
            c = ff(self.D["c"].g())
            if c<=0: raise ValueError("C > 0")
            k = self.kd.get(); out = []
            if k=="sa":
                pH = -math.log10(c)
                out = ["     Strong Acid",
                       f"• [H⁺] = {c} M",
                       f"• pH = {pH:.4f}",
                       f"• pOH = {14-pH:.4f}",
                       f"• [OH⁻] = {10**-(14-pH):.3e} M"]
            elif k=="sb":
                pOH = -math.log10(c); pH = 14-pOH
                out = ["     Strong Base",
                       f"• [OH⁻] = {c} M",
                       f"• pOH = {pOH:.4f}",
                       f"• pH = {pH:.4f}",
                       f"• [H⁺] = {10**-pH:.3e} M"]
            elif k=="wa":
                Ka = ff(self.D["k"].g())
                if Ka<=0: raise ValueError("Ka > 0")
                x = (-Ka + math.sqrt(Ka**2 + 4*Ka*c))/2
                pH = -math.log10(x)
                out = [f"     Weak Acid (Ka = {Ka})",
                       f"• [H⁺] = {x:.6f} M",
                       f"• pH = {pH:.4f}",
                       f"• pKa = {-math.log10(Ka):.4f}",
                       f"• Ionization = {x/c*100:.3f}%"]
            elif k=="wb":
                Kb = ff(self.D["k"].g())
                if Kb<=0: raise ValueError("Kb > 0")
                x = (-Kb + math.sqrt(Kb**2 + 4*Kb*c))/2
                pOH = -math.log10(x); pH = 14-pOH
                out = [f"     Weak Base (Kb = {Kb})",
                       f"• [OH⁻] = {x:.6f} M",
                       f"• pOH = {pOH:.4f}",
                       f"• pH = {pH:.4f}"]
            self.rb.show("\n".join(out)); HIST.add("cat_ph", out[0])
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class BufP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("buf"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        ctk.CTkLabel(self, text="pH = pKa + log([A⁻]/[HA])",
                     font=("Tahoma",15,"italic"),
                     text_color=("#1a73e8","#4da3ff")).pack(pady=(0,10))
        self.fr, self.D = mkform(self, [
            ("pka", tr("lbl_pka"), tr("ph_pka"), 130),
            ("ph", tr("lbl_ph"), tr("ph_ph"), 130),
            ("ct", tr("lbl_ct"), tr("ph_c2"), 150),
            ("v", tr("lbl_v"), tr("ph_v"), 130)])
        ctk.CTkButton(self, text=tr("calc"), font=("Tahoma",14,"bold"),
                      height=40, width=220, command=self.go).pack(pady=10)
        self.rb = RB(self, 270)
        self.rb.pack(fill="both", expand=True, padx=20, pady=(5,15))
    def go(self):
        try:
            pka = ff(self.D["pka"].g()); ph = ff(self.D["ph"].g())
            ct = ff(self.D["ct"].g()); v = ff(self.D["v"].g())
            vL = v/1000
            r = 10**(ph-pka); cA = ct*r/(1+r); cHA = ct-cA
            out = [f"     pKa = {pka}, pH = {ph}",
                   f"• [A⁻]/[HA] = {r:.4f}", "",
                   "      Concentrations:",
                   f"• [A⁻] = {cA:.4f} M",
                   f"• [HA] = {cHA:.4f} M", "",
                   f"         Moles in {v:.0f} mL:",
                   f"• A⁻ = {cA*vL:.6f} mol",
                   f"• HA = {cHA*vL:.6f} mol", "",
                   "   Within range" if pka-1<=ph<=pka+1 else "    Outside (pKa±1)"]
            self.rb.show("\n".join(out)); HIST.add("cat_buf", out[0])
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class MWP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("mw"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        self.fr, self.D = mkform(self, [
            ("f", tr("lbl_formula"), tr("ph_formula"), 350)])
        ctk.CTkButton(self, text=tr("calc"), font=("Tahoma",14,"bold"),
                      height=40, width=200, command=self.go).pack(pady=8)
        ex = ctk.CTkFrame(self, fg_color="transparent"); ex.pack(pady=5)
        ctk.CTkLabel(ex, text=tr("ex"), font=("Tahoma",11)
                     ).pack(side=sd(), padx=5)
        for e in ["H2SO4","NaOH","CuSO4·5H2O","Ca(OH)2","KMnO4",
                  "NaCl","C6H12O6","Fe2(SO4)3"]:
            ctk.CTkButton(ex, text=e, width=85, height=26,
                          font=("Tahoma",10),
                          fg_color=("#d0e0f0","#2a3550"),
                          text_color=("black","white"),
                          command=lambda x=e:(self.D["f"].s(x), self.go())
                          ).pack(side=sd(), padx=2)
        self.rb = RB(self, 290)
        self.rb.pack(fill="both", expand=True, padx=20, pady=(5,15))
    def go(self):
        try:
            f = self.D["f"].g().strip()
            mw = pf(f); cnt = ce(f)
            out = [f"     Formula: {f}",
                   f"         MW = {mw:.4f} g/mol", "",
                   "         Elements:"]
            for sy, n in sorted(cnt.items(),
                                key=lambda x:-AM.get(x[0],0)*x[1]):
                mc = AM.get(sy,0)*n
                out.append(f"  • {sy:3s} × {n:2d} = {mc:9.3f} ({mc/mw*100:6.2f}%)")
            self.rb.show("\n".join(out))
            HIST.add("cat_mw", f"{f} = {mw:.4f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class StatP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("stat"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        ctk.CTkLabel(self, text=tr("stat_note"), font=("Tahoma",12),
                     text_color=("#666","#aaa")).pack()
        self.inp = ctk.CTkTextbox(self, height=100, font=("Consolas",13),
                                  corner_radius=10)
        self.inp.pack(fill="x", padx=20, pady=10)
        self.inp.insert("1.0","10.2, 10.5, 9.8, 10.1, 10.3, 9.9, 10.4, 10.0")
        b = ctk.CTkFrame(self, fg_color="transparent"); b.pack(pady=5)
        ctk.CTkButton(b, text=tr("calc"), font=("Tahoma",13,"bold"),
                      height=38, width=140, command=self.go
                      ).pack(side=sd(), padx=5)
        ctk.CTkButton(b, text=tr("clear"), font=("Tahoma",13),
                      height=38, width=100, fg_color=("#a55","#803030"),
                      command=self.clr).pack(side=sd(), padx=5)
        self.rb = RB(self, 290)
        self.rb.pack(fill="both", expand=True, padx=20, pady=(5,15))
    def clr(self):
        self.inp.delete("1.0","end"); self.rb.clr()
    def go(self):
        try:
            raw = self.inp.get("1.0","end")
            nums = [float(x) for x in re.split(r'[,\s;]+',raw) if x.strip()]
            if len(nums)<2: raise ValueError("≥2 values")
            n = len(nums); mean = statistics.mean(nums)
            med = statistics.median(nums)
            try: mode = f"{statistics.mode(nums)}"
            except: mode = "-"
            sds = statistics.stdev(nums); sdp = statistics.pstdev(nums)
            vs = statistics.variance(nums); vp = statistics.pvariance(nums)
            sem = sds/math.sqrt(n); rng = max(nums)-min(nums)
            cv = sds/mean*100 if mean else 0
            tt = {1:12.706,2:4.303,3:3.182,4:2.776,5:2.571,6:2.447,
                  7:2.365,8:2.306,9:2.262,10:2.228}
            t95 = tt.get(n-1,1.96); ci = t95*sem
            out = ["      Descriptive Statistics","─"*42,
                   f"  n           : {n}",
                   f"  Sum         : {sum(nums):.6f}",
                   f"  Mean        : {mean:.6f}",
                   f"  Median      : {med:.6f}",
                   f"  Mode        : {mode}",
                   f"  Min         : {min(nums):.6f}",
                   f"  Max         : {max(nums):.6f}",
                   f"  Range       : {rng:.6f}","",
                   "    Dispersion","─"*42,
                   f"  SD (sample) : {sds:.6f}",
                   f"  SD (pop)    : {sdp:.6f}",
                   f"  Var (sample): {vs:.6f}",
                   f"  Var (pop)   : {vp:.6f}",
                   f"  SEM         : {sem:.6f}",
                   f"  CV%         : {cv:.4f}%","",
                   f"       95% CI (t = {t95})","─"*42,
                   f"  Mean ± {ci:.6f}",
                   f"  [{mean-ci:.6f} , {mean+ci:.6f}]",""]
            if cv<5: out.append("   Excellent (CV < 5%)")
            elif cv<10: out.append("  Acceptable")
            else: out.append("    Poor")
            self.rb.show("\n".join(out))
            HIST.add("cat_stat", f"n={n}, mean={mean:.4f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class ValP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("val"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        tb = ctk.CTkTabview(self, corner_radius=12)
        tb.pack(fill="both", expand=True, padx=20, pady=10)
        tb.add(tr("v_lin")); tb.add(tr("v_acc")); tb.add(tr("v_prec"))
        tb.add(tr("v_lod")); tb.add(tr("v_sys")); tb.add(tr("v_anova"))
        self._lin(tb.tab(tr("v_lin")))
        self._acc(tb.tab(tr("v_acc")))
        self._prec(tb.tab(tr("v_prec")))
        self._lod(tb.tab(tr("v_lod")))
        self._sys(tb.tab(tr("v_sys")))
        self._anova(tb.tab(tr("v_anova")))

    def _lin(self, t):
        ctk.CTkLabel(t, text="y = mx + b  |  R² = 1 - SSres/SStot",
                     font=("Tahoma",12,"italic"),
                     text_color=("#888","#999")).pack(pady=8)
        f = ctk.CTkFrame(t, fg_color="transparent")
        f.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(f, text=tr("v_conc"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.lx = ctk.CTkEntry(f, height=36, font=("Consolas",12))
        self.lx.pack(fill="x", pady=(2,10))
        self.lx.insert(0, "0, 15.62, 31.25, 62.5, 125")
        ctk.CTkLabel(f, text=tr("v_area"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.ly = ctk.CTkEntry(f, height=36, font=("Consolas",12))
        self.ly.pack(fill="x", pady=(2,10))
        self.ly.insert(0, "0, 758603, 1427232, 3323350, 6168455")
        ctk.CTkButton(t, text=tr("v_calc_lin"), font=("Tahoma",13,"bold"),
                      height=40, width=220, command=self._c_lin).pack(pady=10)
        self.lo = RB(t, 280)
        self.lo.pack(fill="both", expand=True, padx=20, pady=10)

    def _c_lin(self):
        try:
            xs = [float(x) for x in re.split(r'[,\s;]+',self.lx.get()) if x.strip()]
            ys = [float(x) for x in re.split(r'[,\s;]+',self.ly.get()) if x.strip()]
            if len(xs)<2 or len(xs)!=len(ys):
                raise ValueError(tr("check_inputs"))
            n = len(xs); xb = sum(xs)/n; yb = sum(ys)/n
            sxx = sum((x-xb)**2 for x in xs)
            sxy = sum((xs[i]-xb)*(ys[i]-yb) for i in range(n))
            sl = sxy/sxx; ic = yb - sl*xb
            ssr = sum((ys[i]-(sl*xs[i]+ic))**2 for i in range(n))
            sst = sum((y-yb)**2 for y in ys)
            r2 = 1 - ssr/sst if sst else 0
            sdr = math.sqrt(ssr/(n-2)) if n>2 else 0
            lod = 3.3*sdr/abs(sl) if sl else 0
            loq = 10*sdr/abs(sl) if sl else 0
            out = [f"    {tr('v_lin')}","─"*45,
                   f"  n              = {n}",
                   f"  {tr('v_slope'):14s} = {sl:.6f}",
                   f"  {tr('v_int'):14s} = {ic:.4f}",
                   f"  {tr('v_r2'):14s} = {r2:.6f}","",
                   f"  {tr('v_eq')}:",
                   f"     y = {sl:.4f}x + {ic:.4f}","",
                   f"  SD residuals   = {sdr:.4f}",
                   f"  {tr('v_lod_r')}          = {lod:.4f} µg/mL",
                   f"  {tr('v_loq_r')}          = {loq:.4f} µg/mL","","─"*45,
                   tr("v_ok") if r2>=0.995 else tr("v_no")]
            self.lo.show("\n".join(out)); HIST.add("cat_val", f"R²={r2:.6f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _acc(self, t):
        ctk.CTkLabel(t, text="Recovery % = (Measured/Expected)×100",
                     font=("Tahoma",12,"italic"),
                     text_color=("#888","#999")).pack(pady=8)
        f = ctk.CTkFrame(t, fg_color="transparent")
        f.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(f, text=tr("v_exp"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.ae = ctk.CTkEntry(f, height=36); self.ae.pack(fill="x", pady=(2,10))
        self.ae.insert(0, "35.16")
        ctk.CTkLabel(f, text=tr("v_meas"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.am = ctk.CTkEntry(f, height=36); self.am.pack(fill="x", pady=(2,10))
        self.am.insert(0, "35.55")
        ctk.CTkButton(t, text=tr("v_calc_rec"), font=("Tahoma",13,"bold"),
                      height=40, width=220, command=self._c_acc).pack(pady=10)
        self.ao = RB(t, 280)
        self.ao.pack(fill="both", expand=True, padx=20, pady=10)

    def _c_acc(self):
        try:
            e = ff(self.ae.get()); m = ff(self.am.get())
            if e<=0: raise ValueError("E > 0")
            r = m/e*100
            out = [f"       {tr('v_acc')}","─"*45,
                   f"  {tr('v_exp'):15s} = {e}",
                   f"  {tr('v_meas'):15s} = {m}",
                   f"  {tr('v_rec'):15s} = {r:.4f}%","","─"*45,
                   tr("v_rec_ok") if 98<=r<=102 else tr("v_rec_no")]
            self.ao.show("\n".join(out)); HIST.add("cat_val", f"Recovery={r:.2f}%")
        except Exception as ex:
            messagebox.showerror(tr("error"), str(ex))

    def _prec(self, t):
        ctk.CTkLabel(t, text="RSD% = (SD/Mean)×100 | Intraday ≤2% Interday ≤3%",
                     font=("Tahoma",11,"italic"),
                     text_color=("#888","#999")).pack(pady=8)
        f = ctk.CTkFrame(t, fg_color="transparent")
        f.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(f, text=tr("v_values"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.pv = ctk.CTkEntry(f, height=36); self.pv.pack(fill="x", pady=(2,10))
        self.pv.insert(0, "573051, 577415, 574895, 571157")
        ctk.CTkButton(t, text=tr("v_calc_pr"), font=("Tahoma",13,"bold"),
                      height=40, width=220, command=self._c_prec).pack(pady=10)
        self.po = RB(t, 280)
        self.po.pack(fill="both", expand=True, padx=20, pady=10)

    def _c_prec(self):
        try:
            v = [float(x) for x in re.split(r'[,\s;]+',self.pv.get()) if x.strip()]
            if len(v)<2: raise ValueError(tr("check_inputs"))
            n = len(v); m = statistics.mean(v); s = statistics.stdev(v)
            r = s/m*100
            out = [f"      {tr('v_prec')}","─"*45,
                   f"  n        = {n}",
                   f"  {tr('v_mean'):8s} = {m:.4f}",
                   f"  {tr('v_sd'):8s} = {s:.4f}",
                   f"  {tr('v_rsd'):8s} = {r:.4f}%","","─"*45]
            if r<=2: out.append("   Intraday OK (RSD ≤ 2%)")
            elif r<=3: out.append("   Interday OK (RSD ≤ 3%)")
            else: out.append(tr("v_pr_no"))
            self.po.show("\n".join(out)); HIST.add("cat_val", f"RSD={r:.3f}%")
        except Exception as ex:
            messagebox.showerror(tr("error"), str(ex))

    def _lod(self, t):
        ctk.CTkLabel(t, text="LOD = 3.3σ/S  |  LOQ = 10σ/S",
                     font=("Tahoma",12,"italic"),
                     text_color=("#888","#999")).pack(pady=8)
        f = ctk.CTkFrame(t, fg_color="transparent")
        f.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(f, text=tr("v_sigma"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.ls = ctk.CTkEntry(f, height=36); self.ls.pack(fill="x", pady=(2,10))
        self.ls.insert(0, "9739")
        ctk.CTkLabel(f, text=tr("v_slope_s"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.lsl = ctk.CTkEntry(f, height=36); self.lsl.pack(fill="x", pady=(2,10))
        self.lsl.insert(0, "50002.97")
        ctk.CTkButton(t, text=tr("v_calc_lod"), font=("Tahoma",13,"bold"),
                      height=40, width=220, command=self._c_lod).pack(pady=10)
        self.ldo = RB(t, 240)
        self.ldo.pack(fill="both", expand=True, padx=20, pady=10)

    def _c_lod(self):
        try:
            s = ff(self.ls.get()); sl = ff(self.lsl.get())
            if sl==0: raise ValueError("Slope ≠ 0")
            lod = 3.3*s/abs(sl); loq = 10*s/abs(sl)
            out = ["    LOD & LOQ","─"*45,
                   f"  σ = {s}", f"  S = {sl}","",
                   f"  {tr('v_lod_r')}: 3.3 × {s} / {abs(sl)} = {lod:.4f} µg/mL",
                   f"  {tr('v_loq_r')}: 10 × {s} / {abs(sl)} = {loq:.4f} µg/mL","",
                   "─"*45, "   ICH Q2(R1)"]
            self.ldo.show("\n".join(out))
            HIST.add("cat_val", f"LOD={lod:.4f}, LOQ={loq:.4f}")
        except Exception as ex:
            messagebox.showerror(tr("error"), str(ex))

    def _sys(self, t):
        ctk.CTkLabel(t, text="N = 16×(tR/W)²  |  Rs = 2×(tR₂-tR₁)/(W₁+W₂)",
                     font=("Tahoma",11,"italic"),
                     text_color=("#888","#999")).pack(pady=8)
        fn = ctk.CTkFrame(t, corner_radius=10, fg_color=("#ebebeb","#1f2025"))
        fn.pack(fill="x", padx=20, pady=6)
        ctk.CTkLabel(fn, text=f"    {tr('v_N')}", font=("Tahoma",13,"bold"),
                     text_color=("#1a73e8","#4da3ff")
                     ).pack(anchor=anc(), padx=15, pady=(10,5))
        rn = ctk.CTkFrame(fn, fg_color="transparent"); rn.pack(pady=5)
        ctk.CTkLabel(rn, text=tr("v_tR")+":", font=("Tahoma",12)
                     ).pack(side=sd(), padx=5)
        self.nrt = ctk.CTkEntry(rn, width=120, height=34, justify=jst())
        self.nrt.pack(side=sd(), padx=5); self.nrt.insert(0, "2.243")
        ctk.CTkLabel(rn, text=tr("v_W")+":", font=("Tahoma",12)
                     ).pack(side=sd(), padx=(15,0))
        self.nw = ctk.CTkEntry(rn, width=120, height=34, justify=jst())
        self.nw.pack(side=sd(), padx=5); self.nw.insert(0, "0.19179")
        ctk.CTkButton(fn, text=tr("v_calc_N"), font=("Tahoma",12,"bold"),
                      height=36, width=180, command=self._c_N).pack(pady=10)
        fr = ctk.CTkFrame(t, corner_radius=10, fg_color=("#ebebeb","#1f2025"))
        fr.pack(fill="x", padx=20, pady=6)
        ctk.CTkLabel(fr, text=f"      {tr('v_Rs')}", font=("Tahoma",13,"bold"),
                     text_color=("#1a73e8","#4da3ff")
                     ).pack(anchor=anc(), padx=15, pady=(10,5))
        rr = ctk.CTkFrame(fr, fg_color="transparent"); rr.pack(pady=5)
        for lb, attr, dv in [(tr("v_tR1"),"rt1","2.243"),
                             (tr("v_tR2"),"rt2","3.648"),
                             (tr("v_W1"),"w1","0.19179"),
                             (tr("v_W2"),"w2","0.2581")]:
            ctk.CTkLabel(rr, text=lb+":", font=("Tahoma",12)
                         ).pack(side=sd(), padx=3)
            e = ctk.CTkEntry(rr, width=85, height=34, justify=jst())
            e.pack(side=sd(), padx=3); e.insert(0, dv)
            setattr(self, attr, e)
        ctk.CTkButton(fr, text=tr("v_calc_Rs"), font=("Tahoma",12,"bold"),
                      height=36, width=180, command=self._c_Rs).pack(pady=10)
        self.so = RB(t, 180)
        self.so.pack(fill="both", expand=True, padx=20, pady=10)

    def _c_N(self):
        try:
            tR = ff(self.nrt.get()); W = ff(self.nw.get())
            if W<=0: raise ValueError("W > 0")
            N = 16*(tR/W)**2
            out = [f"    {tr('v_N')}","─"*45,
                   f"  tR = {tR}, W = {W}",
                   f"  N = 16 × ({tR}/{W})² = {N:.2f}","",
                   tr("v_N_ok") if N>2000 else tr("v_N_no")]
            self.so.show("\n".join(out)); HIST.add("cat_val", f"N={N:.2f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _c_Rs(self):
        try:
            rt1 = ff(self.rt1.get()); rt2 = ff(self.rt2.get())
            w1 = ff(self.w1.get()); w2 = ff(self.w2.get())
            if (w1+w2)<=0: raise ValueError("W > 0")
            Rs = 2*(rt2-rt1)/(w1+w2)
            out = [f"      {tr('v_Rs')}","─"*45,
                   f"  tR₁={rt1}, tR₂={rt2}",
                   f"  W₁={w1}, W₂={w2}",
                   f"  Rs = 2×({rt2}-{rt1})/({w1}+{w2}) = {Rs:.4f}","",
                   tr("v_Rs_ok") if Rs>1.5 else tr("v_Rs_no")]
            self.so.show("\n".join(out)); HIST.add("cat_val", f"Rs={Rs:.3f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _anova(self, t):
        ctk.CTkLabel(t, text="One-Way ANOVA: F = MSB / MSW",
                     font=("Tahoma",12,"italic"),
                     text_color=("#888","#999")).pack(pady=8)
        f = ctk.CTkFrame(t, fg_color="transparent")
        f.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(f, text=tr("v_groups"), font=("Tahoma",12),
                     anchor=anc()).pack(anchor=anc())
        self.ain = ctk.CTkTextbox(f, height=120, font=("Consolas",12),
                                  corner_radius=8)
        self.ain.pack(fill="x", pady=(2,10))
        self.ain.insert("1.0",
            "15.5847, 31.5275, 62.7135, 125.3673\n"
            "15.6113, 31.3891, 62.6393, 125.3385\n"
            "15.5443, 31.9208, 62.7083, 125.4250")
        ctk.CTkButton(t, text=tr("v_calc_anova"), font=("Tahoma",13,"bold"),
                      height=40, width=220, command=self._c_anova).pack(pady=10)
        self.ao2 = RB(t, 300)
        self.ao2.pack(fill="both", expand=True, padx=20, pady=10)

    def _c_anova(self):
        try:
            raw = self.ain.get("1.0","end").strip()
            lines = [ln for ln in raw.split("\n") if ln.strip()]
            g = []
            for ln in lines:
                v = [float(x) for x in re.split(r'[,\s;]+',ln) if x.strip()]
                if v: g.append(v)
            k = len(g)
            if k<2: raise ValueError("≥2 groups")
            av = [x for gr in g for x in gr]; N = len(av)
            gm = sum(av)/N
            ssb = sum(len(gr)*(statistics.mean(gr)-gm)**2 for gr in g)
            ssw = sum(sum((x-statistics.mean(gr))**2 for x in gr) for gr in g)
            sst = ssb+ssw
            dfb = k-1; dfw = N-k
            msb = ssb/dfb if dfb>0 else 0
            msw = ssw/dfw if dfw>0 else 0
            F = msb/msw if msw>0 else 0
            ft = {(2,6):5.143,(2,8):4.459,(3,8):4.066,(3,9):3.863,
                  (3,11):3.587,(4,8):3.837}
            fc = ft.get((dfb,dfw),3.89)
            out = ["       One-Way ANOVA","─"*50,
                   f"  k = {k}, N = {N}","",
                   f"  {tr('v_ssb'):14s} = {ssb:.6f}",
                   f"  {tr('v_ssw'):14s} = {ssw:.6f}",
                   f"  SS Total       = {sst:.6f}","",
                   f"  dfB = {dfb}, dfW = {dfw}","",
                   f"  {tr('v_msb'):6s} = {msb:.6f}",
                   f"  {tr('v_msw'):6s} = {msw:.6f}",
                   f"  {tr('v_f'):6s} = {F:.6f}",
                   f"  {tr('v_fc'):6s} = {fc}","","─"*50,
                   tr("v_sig") if F>fc else tr("v_nosig")]
            self.ao2.show("\n".join(out))
            HIST.add("cat_val", f"ANOVA F={F:.4f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class PhyP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("phy"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        tb = ctk.CTkTabview(self, corner_radius=12)
        tb.pack(fill="both", expand=True, padx=20, pady=10)
        tb.add(tr("p_dens")); tb.add(tr("p_gas"))
        tb.add(tr("p_beer")); tb.add(tr("p_stock"))
        t = tb.tab(tr("p_dens"))
        f = ctk.CTkFrame(t, fg_color="transparent"); f.pack(pady=20)
        self.dm = F(f, tr("lbl_mass"), tr("ph_mass"))
        self.dv = F(f, tr("lbl_vol"), tr("ph_vol"))
        self.dm.grid(row=0,column=0,padx=10)
        self.dv.grid(row=0,column=1,padx=10)
        ctk.CTkButton(t, text=tr("calc"), font=("Tahoma",13,"bold"),
                      height=38, width=200, command=self._dens).pack(pady=10)
        self.do = RB(t, 150)
        self.do.pack(fill="both", expand=True, padx=20, pady=10)
        t = tb.tab(tr("p_gas"))
        ctk.CTkLabel(t, text="P·V = n·R·T (R=0.08206)",
                     font=("Tahoma",13,"italic")).pack(pady=10)
        f = ctk.CTkFrame(t, fg_color="transparent"); f.pack(pady=10)
        self.gp = F(f, "P (atm)", "—", 110)
        self.gv = F(f, "V (L)", "—", 110)
        self.gn = F(f, "n (mol)", "—", 110)
        self.gt = F(f, "T (K)", "—", 110)
        self.gp.grid(row=0,column=0,padx=5)
        self.gv.grid(row=0,column=1,padx=5)
        self.gn.grid(row=0,column=2,padx=5)
        self.gt.grid(row=0,column=3,padx=5)
        ctk.CTkLabel(t, text=tr("note_empty"), font=("Tahoma",11),
                     text_color=("#888","#999")).pack(pady=5)
        ctk.CTkButton(t, text=tr("calc"), font=("Tahoma",13,"bold"),
                      height=38, width=200, command=self._gas).pack(pady=8)
        self.go_ = RB(t, 150)
        self.go_.pack(fill="both", expand=True, padx=20, pady=10)
        t = tb.tab(tr("p_beer"))
        ctk.CTkLabel(t, text="A = ε · b · c", font=("Tahoma",14,"italic")
                     ).pack(pady=10)
        f = ctk.CTkFrame(t, fg_color="transparent"); f.pack(pady=10)
        self.ba = F(f, "A", "—", 110)
        self.be = F(f, "ε (L/mol·cm)", "—", 130)
        self.bb = F(f, "b (cm)", "—", 110)
        self.bc = F(f, "c (M)", "—", 110)
        self.ba.grid(row=0,column=0,padx=5)
        self.be.grid(row=0,column=1,padx=5)
        self.bb.grid(row=0,column=2,padx=5)
        self.bc.grid(row=0,column=3,padx=5)
        ctk.CTkLabel(t, text=tr("note_empty"), font=("Tahoma",11),
                     text_color=("#888","#999")).pack(pady=5)
        ctk.CTkButton(t, text=tr("calc"), font=("Tahoma",13,"bold"),
                      height=38, width=200, command=self._beer).pack(pady=8)
        self.bo = RB(t, 150)
        self.bo.pack(fill="both", expand=True, padx=20, pady=10)
        t = tb.tab(tr("p_stock"))
        f = ctk.CTkFrame(t, fg_color="transparent"); f.pack(pady=10)
        self.sc1 = F(f, "C₁ (M)", "1", 130)
        self.sc2 = F(f, "C₂ (M)", "0.1", 130)
        self.sv2 = F(f, "V₂ (mL)", "500", 130)
        self.sp = F(f, "Purity %", "100", 110)
        self.sc1.grid(row=0,column=0,padx=6)
        self.sc2.grid(row=0,column=1,padx=6)
        self.sv2.grid(row=0,column=2,padx=6)
        self.sp.grid(row=0,column=3,padx=6)
        ctk.CTkButton(t, text=tr("calc"), font=("Tahoma",13,"bold"),
                      height=38, width=200, command=self._stock).pack(pady=8)
        self.so2 = RB(t, 150)
        self.so2.pack(fill="both", expand=True, padx=20, pady=10)

    def _dens(self):
        try:
            m = ff(self.dm.g()); v = ff(self.dv.g())
            if v<=0: raise ValueError("V > 0")
            d = m/v
            self.do.show("\n".join([f"     ρ = m/V",
                f"• ρ = {m} ÷ {v} = {d:.4f} g/mL",
                f"• = {d*1000:.2f} kg/m³"]))
            HIST.add("cat_dens", f"ρ = {d:.4f}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _gas(self):
        try:
            R = 0.08206
            v = {"P":self.gp.g(),"V":self.gv.g(),"n":self.gn.g(),"T":self.gt.g()}
            emp = [k for k,x in v.items() if not x.strip()]
            if len(emp)!=1: raise ValueError(tr("note_empty"))
            n = {k:ff(x) for k,x in v.items() if x.strip()}
            k = emp[0]
            if k=="P": r = n["n"]*R*n["T"]/n["V"]; msg = f"     P = {r:.4f} atm"
            elif k=="V": r = n["n"]*R*n["T"]/n["P"]; msg = f"     V = {r:.4f} L"
            elif k=="n": r = n["P"]*n["V"]/(R*n["T"]); msg = f"     n = {r:.6f} mol"
            else: r = n["P"]*n["V"]/(R*n["n"]); msg = f"     T = {r:.4f} K = {r-273.15:.2f} °C"
            self.go_.show(msg); HIST.add("cat_gas", msg)
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _beer(self):
        try:
            v = {"A":self.ba.g(),"e":self.be.g(),"b":self.bb.g(),"c":self.bc.g()}
            emp = [k for k,x in v.items() if not x.strip()]
            if len(emp)!=1: raise ValueError(tr("note_empty"))
            n = {k:ff(x) for k,x in v.items() if x.strip()}
            k = emp[0]
            if k=="A": r = n["e"]*n["b"]*n["c"]; msg = f"     A = {r:.4f}"
            elif k=="e": r = n["A"]/(n["b"]*n["c"]); msg = f"     ε = {r:.4f}"
            elif k=="b": r = n["A"]/(n["e"]*n["c"]); msg = f"     b = {r:.4f} cm"
            else: r = n["A"]/(n["e"]*n["b"]); msg = f"     c = {r:.6f} M"
            self.bo.show(msg); HIST.add("cat_beer", msg)
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _stock(self):
        try:
            c1 = ff(self.sc1.g()); c2 = ff(self.sc2.g())
            v2 = ff(self.sv2.g()); p = ff(self.sp.g())/100
            if p<=0: raise ValueError("P > 0")
            v1 = c2*v2/c1; v1c = v1/p
            out = [f"     C₁V₁ = C₂V₂",
                   f"• Take {v1:.4f} mL of {c1} M",
                   f"• Dilute to {v2:.2f} mL"]
            if p<1: out += ["", f"  With purity {p*100:.2f}%:",
                            f"• Take {v1c:.4f} mL"]
            self.so2.show("\n".join(out))
            HIST.add("cat_stock", out[0])
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class UC(ctk.CTkFrame):
    def __init__(self, m, u, note):
        super().__init__(m, fg_color="transparent")
        self.u = u
        ctk.CTkLabel(self, text=note, font=("Tahoma",11),
                     text_color=("#666","#aaa")).pack(pady=8)
        r = ctk.CTkFrame(self, fg_color="transparent"); r.pack(pady=15)
        ctk.CTkLabel(r, text=tr("u_from"), font=("Tahoma",13)
                     ).pack(side=sd(), padx=5)
        self.fu = ctk.CTkOptionMenu(r, values=list(u.keys()), width=220)
        self.fu.pack(side=sd(), padx=8)
        ctk.CTkLabel(r, text=tr("u_val"), font=("Tahoma",13)
                     ).pack(side=sd(), padx=5)
        self.ve = ctk.CTkEntry(r, width=160, height=36, font=("Tahoma",14),
                               justify=jst())
        self.ve.pack(side=sd(), padx=8)
        ctk.CTkButton(self, text=tr("u_conv"), font=("Tahoma",13,"bold"),
                      height=38, width=180, command=self.go).pack(pady=10)
        self.o = RB(self, 240)
        self.o.pack(fill="both", expand=True, padx=20, pady=10)
    def go(self):
        try:
            v = ff(self.ve.get()); s = self.fu.get()
            b = v*self.u[s]
            L = [f"     {v} {s}","─"*42]
            for nm, f_ in self.u.items():
                r = b/f_
                mk = "  ◀" if nm == s else ""
                L.append(f"  {nm:28s} = {r:.6g}{mk}")
            self.o.show("\n".join(L))
            HIST.add("cat_conv", f"{v} {s}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

class UntP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("unt"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        tb = ctk.CTkTabview(self, corner_radius=12)
        tb.pack(fill="both", expand=True, padx=20, pady=10)
        tb.add(tr("u_vol")); tb.add(tr("u_mass"))
        tb.add(tr("u_pres")); tb.add(tr("u_temp")); tb.add(tr("u_conc"))
        UC(tb.tab(tr("u_vol")), {
            "L":1.0,"mL":1e-3,"µL":1e-6,"nL":1e-9,
            "gal":3.78541,"qt":0.946353,"pt":0.473176,
            "fl oz":0.0295735,"m³":1000.0,"cm³":1e-3,
        }, "Base: L").pack(fill="both", expand=True)
        UC(tb.tab(tr("u_mass")), {
            "kg":1.0,"g":1e-3,"mg":1e-6,"µg":1e-9,
            "ng":1e-12,"lb":0.453592,"oz":0.0283495,"t":1000.0,
        }, "Base: kg").pack(fill="both", expand=True)
        UC(tb.tab(tr("u_pres")), {
            "atm":1.0,"bar":0.986923,"mbar":9.86923e-4,
            "Pa":9.86923e-6,"kPa":9.86923e-3,"MPa":9.86923,
            "mmHg":1/760,"Torr":1/760,"psi":1/14.6959,
        }, "Base: atm").pack(fill="both", expand=True)
        self._temp(tb.tab(tr("u_temp")))
        self._conc(tb.tab(tr("u_conc")))

    def _temp(self, t):
        ctk.CTkLabel(t, text=tr("u_temp_note"), font=("Tahoma",11),
                     text_color=("#666","#aaa")).pack(pady=8)
        r = ctk.CTkFrame(t, fg_color="transparent"); r.pack(pady=15)
        ctk.CTkLabel(r, text=tr("u_val"), font=("Tahoma",13)
                     ).pack(side=sd(), padx=5)
        self.te = ctk.CTkEntry(r, width=160, height=36, font=("Tahoma",14),
                               justify=jst())
        self.te.pack(side=sd(), padx=8)
        ctk.CTkLabel(r, text=tr("u_unit"), font=("Tahoma",13)
                     ).pack(side=sd(), padx=5)
        self.tu = ctk.CTkOptionMenu(r, values=["°C","°F","K"], width=100)
        self.tu.pack(side=sd(), padx=8)
        ctk.CTkButton(t, text=tr("u_conv_temp"), font=("Tahoma",13,"bold"),
                      height=38, width=180, command=self._do_temp).pack(pady=10)
        self.to = RB(t, 200)
        self.to.pack(fill="both", expand=True, padx=20, pady=10)

    def _do_temp(self):
        try:
            v = ff(self.te.get()); u = self.tu.get()
            if u=="°C": c,f,k = v, v*9/5+32, v+273.15
            elif u=="°F": c = (v-32)*5/9; f = v; k = c+273.15
            else: c = v-273.15; f = c*9/5+32; k = v
            self.to.show(f"     {v} {u}\n" + "─"*42 + "\n"
                         f"  Celsius    = {c:.4f} °C\n"
                         f"  Fahrenheit = {f:.4f} °F\n"
                         f"  Kelvin     = {k:.4f} K")
            HIST.add("cat_temp", f"{v} {u}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

    def _conc(self, t):
        ctk.CTkLabel(t, text=tr("u_conc_note"), font=("Tahoma",12),
                     text_color=("#666","#aaa")).pack(pady=8)
        f = ctk.CTkFrame(t, fg_color="transparent"); f.pack(pady=10)
        self.cmw = F(f, "MW (g/mol)", tr("ph_mw"), 130)
        self.cm = F(f, "M", "—", 130)
        self.cg = F(f, "g/L", "—", 130)
        self.cp = F(f, "% w/v", "—", 130)
        self.cpm = F(f, "ppm", "—", 130)
        self.cmw.grid(row=0,column=0,padx=6)
        self.cm.grid(row=0,column=1,padx=6)
        self.cg.grid(row=0,column=2,padx=6)
        self.cp.grid(row=0,column=3,padx=6)
        self.cpm.grid(row=0,column=4,padx=6)
        b = ctk.CTkFrame(t, fg_color="transparent"); b.pack(pady=8)
        ctk.CTkButton(b, text=tr("u_conv_conc"), font=("Tahoma",13,"bold"),
                      height=38, width=180, command=self._do_conc
                      ).pack(side=sd(), padx=5)
        ctk.CTkButton(b, text=tr("clear"), font=("Tahoma",13),
                      height=38, width=100, fg_color=("#a55","#803030"),
                      command=self._clr).pack(side=sd(), padx=5)
        self.co = RB(t, 200)
        self.co.pack(fill="both", expand=True, padx=20, pady=10)

    def _clr(self):
        for f in (self.cmw, self.cm, self.cg, self.cp, self.cpm): f.c()
        self.co.clr()

    def _do_conc(self):
        try:
            mw = ff(self.cmw.g())
            if mw<=0: raise ValueError("MW > 0")
            v = {"M":self.cm.g().strip(),"g/L":self.cg.g().strip(),
                 "%":self.cp.g().strip(),"ppm":self.cpm.g().strip()}
            fl = {k:ff(x) for k,x in v.items() if x}
            if len(fl)!=1: raise ValueError("Fill 1 value only")
            k,x = list(fl.items())[0]
            if k=="M": m=x; gL=m*mw; pct=gL/10; ppm=gL*1000
            elif k=="g/L": gL=x; m=gL/mw; pct=gL/10; ppm=gL*1000
            elif k=="%": pct=x; gL=pct*10; m=gL/mw; ppm=gL*1000
            else: ppm=x; gL=ppm/1000; m=gL/mw; pct=gL/10
            self.co.show("\n".join([
                "     Results:","─"*42,
                f"  M   = {m:.6f}",
                f"  g/L = {gL:.6f}",
                f"  %   = {pct:.6f}",
                f"  ppm = {ppm:.4f}"]))
            HIST.add("cat_conc", f"{k}={x}")
        except Exception as e:
            messagebox.showerror(tr("error"), str(e))

# ═══════════════════════════════════════════════════
class HistP(ctk.CTkFrame):
    def __init__(self, m):
        super().__init__(m, fg_color="transparent")
        ctk.CTkLabel(self, text=tr("hist"), font=("Tahoma",22,"bold")
                     ).pack(pady=(15,8))
        b = ctk.CTkFrame(self, fg_color="transparent"); b.pack(pady=5)
        ctk.CTkButton(b, text=tr("refresh"), font=("Tahoma",13), height=38,
                      width=120, command=self.refresh).pack(side=sd(), padx=5)
        ctk.CTkButton(b, text=tr("export"), font=("Tahoma",13), height=38,
                      width=150, command=self.exp).pack(side=sd(), padx=5)
        ctk.CTkButton(b, text=tr("clr_hist"), font=("Tahoma",13), height=38,
                      width=130, fg_color=("#a55","#803030"),
                      command=self.clr).pack(side=sd(), padx=5)
        self.o = RB(self, 400)
        self.o.pack(fill="both", expand=True, padx=20, pady=(10,15))
        self.refresh()
    def refresh(self):
        if not HIST.rec:
            self.o.show(tr("no_hist")); return
        L = []
        for i,r in enumerate(reversed(HIST.rec),1):
            L.append(f"[{i}] {r['t']}  —  {tr(r['k'])}")
            L.append(f"    {r['d']}"); L.append("")
        self.o.show("\n".join(L))
    def exp(self):
        if not HIST.rec:
            messagebox.showinfo(tr("info"), tr("no_hist")); return
        p = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV","*.csv")],
            initialfile=f"lab_{datetime.now():%Y%m%d_%H%M%S}.csv")
        if p:
            HIST.exp(p)
            messagebox.showinfo(tr("done"),
                                tr("exported", n=len(HIST.rec)))
    def clr(self):
        if messagebox.askyesno(tr("confirm"), tr("clr_q")):
            HIST.rec.clear(); self.refresh()

# ═══════════════════════════════════════════════════
# ═══════════ ةيسيئرلا ةهجاولا (Responsive) ═══════════
# ═══════════════════════════════════════════════════
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        w = max(820,  min(1320, sw - 60))
        h = max(560,  min(840,  sh - 90))
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.minsize(820, 560)
        self._build()

    def _build(self):
        for w in self.winfo_children(): w.destroy()
        self.pages = {}; self.current = None
        self.title(tr("title"))

        # ═══════════ Sidebar ═══════════
        sb = ctk.CTkFrame(self, width=230, corner_radius=0,
                          fg_color=("#1a1c22","#0f1117"))
        sb.pack(side=sd(), fill="y"); sb.pack_propagate(False)

        #  ةكراشملا قوقحو ناونعلا
        head = ctk.CTkFrame(sb, fg_color="transparent")
        head.pack(fill="x", pady=(12, 6))
        ctk.CTkLabel(head, text=f"      {tr('lab')}",
                     font=("Tahoma", 17, "bold"), text_color="#4da3ff"
                     ).pack()
        ctk.CTkLabel(head,
                     text="Mohammad.A.M.Mousa\n(Abdel Qader)",
                     font=("Tahoma", 9, "italic"),
                     text_color=("#ccc","#aaa"),
                     justify="center").pack(pady=(2,0))
        ctk.CTkLabel(head, text="× DeepSeek AI",
                     font=("Tahoma", 9, "italic"),
                     text_color="#4da3ff").pack(pady=(0,2))
        ctk.CTkLabel(head, text="Python 3",
                     font=("Tahoma", 8),
                     text_color=("#888","#666")).pack()

        #  ةغللا رايتخا
        lf = ctk.CTkFrame(sb, fg_color="transparent")
        lf.pack(fill="x", padx=8, pady=(6, 6))
        self.lv = ctk.StringVar(value={"ar":'العربية',"en":"English",
                                        "de":"Deutsch"}[LANG])
        ctk.CTkOptionMenu(lf, values=['العربية',"English","Deutsch"],
                          variable=self.lv, command=self._lang,
                          width=210, height=30).pack()

        #  ريرمتلل ةلباق رارزلأا ةمئاق
        menu = ctk.CTkScrollableFrame(
            sb, fg_color="transparent", corner_radius=0,
            scrollbar_button_color=("#2a3040","#1e2533"))
        menu.pack(fill="both", expand=True, padx=0, pady=0)

        items = [(tr("home"), HomeP), (tr("sol"), SolP),
                 (tr("dil"), DilP), (tr("ph"), PHP),
                 (tr("buf"), BufP), (tr("mw"), MWP),
                 (tr("stat"), StatP), (tr("val"), ValP),
                 (tr("phy"), PhyP), (tr("unt"), UntP),
                 (tr("hist"), HistP)]
        self.btns = []
        for nm, cls in items:
            b = ctk.CTkButton(menu, text=nm, anchor=anc(),
                              font=("Tahoma", 12), height=38, corner_radius=8,
                              fg_color="transparent",
                              hover_color=("#2a3040","#1e2533"),
                              text_color=("#ccc","#ddd"),
                              command=lambda n=nm, c=cls: self._sw(n, c))
            b.pack(fill="x", padx=8, pady=2)
            self.btns.append((nm, b, cls))
        #  ةمئاقلا لفسأ رهظملا رز
        ctk.CTkButton(sb, text=tr("theme"), font=("Tahoma", 11), height=32,
                      fg_color=("#2a3040","#1e2533"),
                      command=self._theme).pack(side="bottom", fill="x",
                                                padx=8, pady=8)

        # ىوتحملا ةقطنم
        self.ct = ctk.CTkScrollableFrame(
            self, fg_color="transparent", corner_radius=0,
            scrollbar_button_color=("#2a3040","#1e2533"))
        self.ct.pack(side=("left" if rtl() else "right"),
                     fill="both", expand=True)
        self._sw(items[0][0], items[0][1])

    def _lang(self, choice):
        global LANG
        new = {'العربية':"ar","English":"en","Deutsch":"de"}.get(choice,"ar")
        if new == LANG: return
        LANG = new
        self._build()

    def _sw(self, nm, cls):
        if self.current is not None:
            self.current.pack_forget()
        if nm not in self.pages:
            try:
                self.pages[nm] = cls(self.ct)
            except Exception as e:
                messagebox.showerror(tr("error"), f"{nm}\n{e}")
                return
        pg = self.pages[nm]
        pg.pack(fill="x", padx=15, pady=15)
        self.current = pg
        if nm == tr("hist"):
            pg.refresh()
        for n, b, _ in self.btns:
            if n == nm:
                b.configure(fg_color=("#1a73e8","#1a73e8"),
                            text_color="white")
            else:
                b.configure(fg_color="transparent",
                            text_color=("#ccc","#ddd"))

    def _theme(self):
        c = ctk.get_appearance_mode()
        ctk.set_appearance_mode("light" if c == "Dark" else "dark")

# ═══════════════════════════════════════════════════
if __name__ == "__main__":
    app = App()
    app.mainloop()
