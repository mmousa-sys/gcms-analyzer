# -*- coding: utf-8 -*-
"""GC-MS Essential Oil Analyzer - KRI Calculator (Full Adams Extended Edition)"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

C = {"bg":"#0f172a","bg2":"#1e293b","card":"#1e293b","card2":"#334155",
     "primary":"#14b8a6","primary2":"#0d9488","accent":"#38bdf8",
     "gold":"#fbbf24","text":"#e2e8f0","muted":"#94a3b8",
     "border":"#334155","ok":"#22c55e","err":"#ef4444"}
AUTHOR_EN = "Mohammad Asad Mohammad Abdel Qader (Mousa)"
AUTHOR_AR = "محمد أسعد محمد عبد القادر (موسى)"
ROLE = {"ar":"فني مختبرات كيميائي","en":"Chemical Laboratory Technician","de":"Chemielaborant"}

# ============================================================
# DATABASE: Adams (2017) ed. 4.1 - Base compounds
# ============================================================
REF_DB = [
# Monoterpene hydrocarbons
("α-Thujene","2867-05-2","C10H16",925.9,927.8,1026.6,924),
("α-Pinene","80-56-8","C10H16",934.5,936.1,1025.4,932),
("Camphene","79-92-5","C10H16",947.4,950.3,1068.5,946),
("Sabinene","3387-41-5","C10H16",967.9,973.0,1122.0,969),
("β-Pinene","127-91-3","C10H16",973.1,977.7,1110.0,974),
("Myrcene","123-35-3","C10H16",983.1,989.2,1160.9,988),
("α-Phellandrene","99-83-2","C10H16",999.1,1004.1,1167.7,1002),
("δ-3-Carene","13466-78-9","C10H16",1007.2,1011.3,1146.8,1001),
("α-Terpinene","99-86-5","C10H16",1010.9,1017.1,1177.8,1014),
("p-Cymene","99-87-6","C10H14",1015.1,1024.3,1270.1,1020),
("Limonene","5989-27-5","C10H16",1023.7,1029.5,1198.2,1024),
("β-Phellandrene","555-10-2","C10H16",1021.4,1030.0,1209.3,1030),
("1,8-Cineole","470-82-6","C10H18O",1022.4,1031.8,1211.1,1026),
("Eucalyptus","470-82-6","C10H18O",1022.4,1031.8,1211.1,1026),
("(Z)-β-Ocimene","3338-55-4","C10H16",1028.9,1037.8,1234.5,1032),
("(E)-β-Ocimene","3779-61-1","C10H16",1038.4,1047.7,1250.4,1044),
("γ-Terpinene","99-85-4","C10H16",1050.3,1059.7,1245.0,1054),
("Terpinolene","586-62-9","C10H16",1079.3,1086.9,1282.4,1086),
("Linalool","78-70-6","C10H18O",1086.3,1099.0,1543.3,1095),
("α-Thujone","546-80-5","C10H16O",1090.9,1105.1,1423.1,1101),
("β-Thujone","471-15-8","C10H16O",1098.4,1114.5,1439.6,1112),
("Camphor","76-22-2","C10H16O",1125.0,1143.4,1515.1,1141),
("Citronellal","106-23-0","C10H18O",1133.6,1153.7,1475.3,1148),
("Isoborneol","124-76-5","C10H18O",1147.8,1158.2,1659.1,1155),
("Borneol","507-70-0","C10H18O",1153.2,1166.2,1699.6,1165),
("Menthone","89-80-5","C10H18O",1136.9,1150.5,1465.3,1148),
("Terpinen-4-ol","562-74-3","C10H18O",1164.5,1177.1,1601.2,1174),
("Menthol","89-78-1","C10H20O",1162.7,1177.3,1630.4,1167),
("α-Terpineol","98-55-5","C10H18O",1175.6,1189.7,1694.0,1186),
("Myrtenal","564-94-3","C10H14O",1170.8,1192.0,1631.5,1195),
("Verbenone","80-57-9","C10H14O",1184.4,1206.2,1720.5,1204),
("Nerol","106-25-2","C10H18O",1216.2,1228.9,1794.6,1227),
("Citronellol","106-22-9","C10H20O",1212.4,1228.1,1763.9,1223),
("Neral","106-26-3","C10H16O",1220.3,1242.1,1678.5,1235),
("Geraniol","106-24-1","C10H18O",1238.9,1254.9,1839.3,1249),
("Geranial","141-27-5","C10H16O",1247.1,1270.3,1725.0,1264),
("Linalyl acetate","115-95-7","C12H20O2",1242.3,1255.2,1554.0,1254),
("Bergamiol","115-95-7","C12H20O2",1242.3,1255.2,1554.0,1254),
("Bornyl acetate","76-49-3","C12H20O2",1270.2,1283.5,1579.3,1284),
("Thymol","89-83-8","C10H14O",1271.8,1290.1,2164.3,1289),
("Carvacrol","499-75-2","C10H14O",1282.7,1300.4,2210.8,1298),
("α-Terpinyl acetate","80-26-2","C12H20O2",1332.8,1347.0,1694.8,1346),
("Neryl acetate","141-12-8","C12H20O2",1343.8,1362.9,1718.1,1359),
("Geranyl acetate","105-87-3","C12H20O2",1361.4,1379.9,1751.1,1379),
("α-Cubebene","17699-14-8","C15H24",1352.2,1351.4,1460.4,1345),
("α-Ylangene","14912-44-8","C15H24",1370.0,1369.9,1484.1,1373),
("α-Copaene","3856-25-5","C15H24",1375.5,1376.2,1491.0,1374),
("β-Bourbonene","5208-59-3","C15H24",1381.7,1384.2,1523.2,1387),
("β-Cubebene","13744-15-5","C15H24",1383.5,1386.6,1541.7,1387),
("β-Elemene","515-13-9","C15H24",1388.0,1390.4,1590.9,1389),
("β-Elemen","515-13-9","C15H24",1388.0,1390.4,1590.9,1389),
("Cyperene","2387-78-2","C15H24",1398.7,1397.8,1528.0,1398),
("β-Caryophyllene","87-44-5","C15H24",1419.3,1420.1,1598.5,1417),
("β-Copaene","18252-44-3","C15H24",1427.3,1433.1,1579.8,1430),
("α-Bergamotene","13474-59-4","C15H24",1431.1,1434.5,1575.7,1432),
("α-trans-Bergamotene","13474-59-4","C15H24",1431.1,1434.5,1575.7,1432),
("Aromadendrene","489-39-4","C15H24",1439.0,1440.6,1620.2,1439),
("α-Gurjunene","489-40-7","C15H24",1409.0,1409.5,1548.0,1410),
("α-Humulene","6753-98-6","C15H24",1449.3,1453.1,1666.7,1452),
("(E)-β-Farnesene","18794-84-8","C15H24",1449.3,1455.9,1663.9,1454),
("allo-Aromadendrene","25246-27-9","C15H24",1459.1,1459.9,1649.2,1458),
("γ-Muurolene","30021-74-0","C15H24",1473.0,1476.2,1689.8,1478),
("Germacrene D","23986-74-5","C15H24",1475.9,1480.6,1708.2,1484),
("β-Selinene","17066-67-0","C15H24",1480.7,1486.1,1716.9,1489),
("δ-Selinene","17066-67-0","C15H24",1480.7,1486.1,1716.9,1489),
("α-Muurolene","31983-22-9","C15H24",1491.0,1498.3,1723.4,1500),
("α-Selinene","473-13-2","C15H24",1489.5,1493.4,1725.3,1498),
("Bicyclogermacrene","24703-35-3","C15H24",1489.8,1494.1,1734.5,1500),
("β-Bisabolene","495-61-4","C15H24",1499.9,1508.4,1727.5,1508),
("γ-Cadinene","39029-41-9","C15H24",1505.7,1513.1,1763.3,1513),
("δ-Cadinene","483-76-1","C15H24",1513.9,1523.2,1755.7,1522),
("α-Calacorene","21391-99-1","C15H20",1530.4,1540.3,1921.4,1544),
("α-Bisabolene","25532-79-0","C15H24",1533.6,1540.3,1775.2,1540),
("β-Sesquiphellandrene","20307-83-9","C15H24",1513.2,1523.5,1771.4,1521),
("α-Zingiberene","495-60-3","C15H24",1482.9,1495.3,1720.7,1493),
("Valencene","4630-07-3","C15H24",1483.0,1491.7,1728.6,1496),
("(E,E)-α-Farnesene","502-61-4","C15H24",1496.3,1504.1,1743.9,1505),
("Cuparene","16982-00-6","C15H22",1504.8,1506.6,1816.1,1504),
("α-Bulnesene","3691-11-0","C15H24",1500.6,1504.1,1629.0,1509),
("α-Longipinene","5989-08-2","C15H24",1350.6,1352.1,1469.0,1350),
("δ-Elemene","20307-84-0","C15H24",1340.3,1337.0,1468.8,1335),
("α-Santalene","512-61-8","C15H24",1415.9,1421.8,1582.7,1416),
("α-Patchoulene","560-32-7","C15H24",1451.3,1457.2,1550.0,1454),
("Nerolidol (Z)","3790-78-1","C15H26O",1524.4,1543.6,2007.3,1531),
("Nerolidol (E)","40716-66-3","C15H26O",1550.1,1560.9,2036.3,1561),
("Spathulenol","6750-60-3","C15H24O",1566.4,1576.4,2126.6,1577),
("Caryophyllene oxide","1139-30-6","C15H24O",1570.0,1580.6,1986.2,1582),
("Globulol","51371-47-2","C15H26O",1578.9,1581.8,2082.4,1590),
("Ledol","577-27-5","C15H26O",1568.0,1582.5,2039.1,1602),
("Viridiflorol","552-02-3","C15H26O",1579.9,1590.8,2089.8,1592),
("Guaiol","489-86-1","C15H26O",1588.9,1597.1,2088.9,1600),
("Cedrol","77-53-2","C15H26O",1597.1,1600.1,2119.6,1600),
("Cubenol","21284-22-0","C15H26O",1619.9,1636.5,2067.8,1645),
("epi-α-Cadinol","5937-11-1","C15H26O",1626.4,1637.8,2169.7,1638),
("α-Cadinol","481-34-5","C15H26O",1640.2,1651.9,2227.3,1652),
("α-Bisabolol","515-69-5","C15H26O",1668.4,1682.8,2213.6,1685),
("β-Bisabolol","15352-77-9","C15H26O",1658.6,1672.0,2143.1,1674),
("(2E,6E)-Farnesol","106-28-5","C15H26O",1709.6,1743.5,2366.0,1742),
("(2Z,6E)-Farnesol","3790-71-4","C15H26O",1704.7,1722.5,2356.8,1722),
("(2E,6Z)-Farnesol","3879-60-5","C15H26O",1691.3,1713.6,2341.0,1714),
("(2Z,6Z)-Farnesol","16106-95-9","C15H26O",1686.9,1694.4,2324.4,1698),
("Nootkatone","4674-50-4","C15H22O",1776.5,1813.4,2548.3,1806),
("Sclareol","515-03-7","C20H36O2",1990.0,2222.0,2600.0,2222),
("Bulnesol","22451-73-6","C15H26O",1653.3,1665.7,2205.3,1670),
("α-Acorenol","28296-85-7","C15H26O",1620.3,1630.0,2163.0,1632),
("Acorenone B","24048-45-1","C15H24O",1682.0,1697.0,2010.0,1697),
("β-Eudesmol","473-15-4","C15H26O",1649.0,1650.1,2238.0,1649),
("α-Eudesmol","473-16-5","C15H26O",1652.0,1651.7,2222.7,1652),
("γ-Eudesmol","1209-71-8","C15H26O",1630.0,1630.9,2176.1,1630),
("10-epi-γ-Eudesmol","15051-81-7","C15H26O",1607.9,1618.7,2105.8,1622),
("Juniperol","465-04-3","C15H26O",1592.2,1591.7,2157.2,1599),
("Cedryl acetate","77-54-3","C17H28O2",1767.0,1767.0,2350.0,1767),
("Patchouli alcohol","5986-55-0","C15H26O",1653.2,1659.8,2156.0,1656),
("Khusimol","24250-85-9","C15H24O",1741.0,1741.0,2350.0,1741),
("α-Vetivone","15764-04-2","C15H22O",1842.0,1842.0,2450.0,1842),
("β-Vetivone","18444-79-6","C15H22O",1822.0,1822.0,2420.0,1822),
("Vetiselinenol","15130-85-5","C15H24O",1730.0,1730.0,2300.0,1730),
("Hinesol","23811-08-7","C15H26O",1640.0,1640.0,2150.0,1640),
("Benzaldehyde","100-52-7","C7H6O",936.6,962.7,1518.7,952),
("Methyl chavicol","140-67-0","C10H12O",1178.1,1195.8,1671.4,1195),
("(E)-Anethole","4180-23-8","C10H12O",1264.7,1285.2,1826.1,1282),
("Eugenol","97-53-0","C10H12O2",1339.6,1357.8,2162.7,1356),
("Methyl eugenol","93-15-2","C11H14O2",1376.1,1401.8,2006.3,1403),
("(E)-Cinnamaldehyde","14371-10-9","C9H8O",1238.6,1271.3,2033.2,1267),
("Benzyl acetate","140-11-4","C9H10O2",1141.1,1165.6,1723.1,1157),
("Benzyl alcohol","100-51-6","C7H8O",1015.4,1036.9,1865.3,1026),
("2-Phenylethyl alcohol","60-12-8","C8H10O",1088.2,1114.9,1903.7,1106),
("Methyl salicylate","119-36-8","C8H8O3",1172.5,1192.9,1767.8,1190),
("Vanillin","121-33-5","C8H8O3",1358.0,1404.7,2569.5,1393),
("Thymol methyl ether","1076-56-8","C11H16O",1214.1,1234.3,1587.2,1232),
("Carvacrol methyl ether","6379-73-3","C11H16O",1221.5,1243.0,1598.9,1241),
("Hexanal","66-25-1","C6H12O",776.9,799.9,1082.0,801),
("(E)-2-Hexenal","6728-26-3","C6H10O",846.0,853.0,1216.3,854),
("(Z)-3-Hexenol","928-96-1","C6H12O",850.0,856.6,1380.2,850),
("1-Hexanol","111-27-3","C6H14O",854.9,869.7,1351.4,863),
("Heptanal","111-71-7","C7H14O",880.7,902.0,1185.1,901),
("Octanal","124-13-0","C8H16O",982.4,1002.8,1287.2,998),
("Nonanal","124-19-6","C9H18O",1083.8,1103.3,1391.5,1100),
("Decanal","112-31-2","C10H20O",1185.7,1205.4,1495.9,1201),
("Benzeneacetaldehyde","122-78-1","C8H8O",1016.1,1045.9,1640.7,1036),
("Furfural","98-01-1","C5H4O2",806.5,834.6,1460.9,828),
("5-Methylfurfural","620-02-0","C6H6O2",933.3,967.3,1573.6,957),
("(E)-β-Damascenone","23726-93-4","C13H18O",1363.4,1385.5,1820.9,1383),
("Jasmone (Z)","488-10-8","C11H16O",1368.9,1394.6,1955.2,1392),
("Methyl jasmonate","1211-29-6","C13H20O3",1648.0,1648.0,2200.0,1648),
("Dihydrojasmone","1128-08-1","C11H18O",1338.0,1338.0,1720.0,1338),
("α-Ionone (E)","127-41-3","C13H20O",1411.2,1425.6,1843.4,1425),
("β-Ionone (E)","79-77-6","C13H20O",1466.2,1485.9,1935.5,1485),
("Geranylacetone","3796-70-1","C13H22O",1431.1,1451.8,1854.9,1453),
("Nootkatol","50764-06-6","C15H24O",1724.0,1730.0,2050.0,1714),
("Cadalene","483-78-3","C15H18",1654.9,1671.3,2233.0,1675),
("Chamazulene","529-05-5","C14H16",1710.0,1726.7,2440.0,1730),
("Abietadiene","19407-28-4","C20H30",2032.8,2054.3,2506.1,2087),
("Manool","596-85-0","C20H34O",2047.5,2057.3,2628.0,2056),
("Manoyl oxide","596-84-9","C20H34O",1990.4,1993.1,2376.0,1987),
("Sclareolide","564-20-5","C16H26O2",2065.0,2065.0,2700.0,2065),
("Phytol","150-86-7","C20H40O",2099.1,2116.4,2613.4,1942),
("Hexadecanoic acid","57-10-3","C16H32O2",1955.4,1968.4,2913.2,1959),
("Octadecanoic acid","57-11-4","C18H36O2",2158.7,2172.4,3148.3,2152),
("Linoleic acid","60-33-3","C18H32O2",2105.0,2128.9,3215.0,2132),
("Oleic acid","112-80-1","C18H34O2",2113.0,2133.2,3200.0,2141),
("(E)-β-Santalene","511-59-1","C15H24",1453.0,1458.5,1644.9,1457),
("Santalol (Z, α)","115-71-9","C15H24O",1674.0,1674.0,2200.0,1674),
("Santalol (E, α)","11031-45-1","C15H24O",1738.0,1738.0,2270.0,1738),
("β-Patchoulene","514-51-2","C15H24",1379.0,1379.0,1450.0,1379),
("α-Springene","13474-59-4","C15H24",1955.0,1958.0,2100.0,1960),
]

# ============================================================
# EXTRA DB - Additional compounds from Adams ed. 4.1
# ============================================================
EXTRA_DB = [
# Additional monoterpene hydrocarbons
("α-Fenchene","471-84-1","C10H16",None,945,None,945),
("Verbenene","4080-46-0","C10H14",None,961,None,961),
("Thuja-2,4(10)-diene","36262-09-6","C10H14",None,953,None,953),
("Isolimonene","511-02-3","C10H16",None,980,None,980),
("Sylvestrene","1461-27-4","C10H16",None,1025,None,1025),
("Mentha-1(7),8-diene <p->","499-97-8","C10H16",None,1003,None,1003),
("Mentha-3,8-diene <p->","586-67-4","C10H16",None,1068,None,1068),
("Mentha-2,4(8)-diene <p->","586-63-0","C10H16",None,1085,None,1085),
("Menthene <1-p->","5502-88-5","C10H18",None,1021,None,1021),
("Pinane <trans->","33626-25-4","C10H18",None,969,None,969),
("Pinane <cis->","6876-13-7","C10H18",None,982,None,982),
("Menthane <trans-p->","1678-82-6","C10H20",None,973,None,973),
("Cymene <o->","527-84-4","C10H14",None,1022,None,1022),
("Cymenene <p->","1195-32-0","C10H12",None,1089,None,1089),
("Ocimene <allo->","7216-56-0","C10H16",None,1128,None,1128),
("Ocimene <neo-allo->","3016-19-1","C10H16",None,1140,None,1140),
("Artemisia triene","18383-70-5","C10H16",None,923,None,923),
("Santolina triene","2153-66-4","C10H16",None,906,None,906),
("Citronellene <β->","2436-90-0","C10H18",None,942,None,942),
("Salvene <E->","33746-69-9","C9H16",None,858,None,858),
("Salvene <Z->","33746-70-2","C9H16",None,847,None,847),
("Tricyclene","508-32-7","C10H16",None,921,None,921),
("Santene","529-16-8","C9H14",None,884,None,884),
("Norbornene","498-66-8","C7H10",None,728,None,728),

# Additional monoterpene alcohols
("1,4-Cineole","470-67-7","C10H18O",None,1012,None,1012),
("Cineole <dehydro-1,8>","66113-06-2","C10H16O",None,988,None,988),
("Linalool <dihydro->","18479-51-1","C10H20O",None,1131,None,1131),
("Linalool <tetrahydro->","78-69-3","C10H22O",None,1098,None,1098),
("Fenchol <endo->","14575-74-7","C10H18O",None,1114,None,1114),
("Fenchol <exo->","22627-95-8","C10H18O",None,1118,None,1118),
("Pinocarveol <cis->","19889-99-7","C10H16O",None,1182,None,1182),
("Pinocarveol <trans->","547-61-5","C10H16O",None,1135,None,1135),
("Verbenol <cis->","1845-30-3","C10H16O",None,1137,None,1137),
("Verbenol <trans->","1820-09-3","C10H16O",None,1140,None,1140),
("Myrtenol","515-00-4","C10H16O",None,1194,None,1194),
("Lavandulol","498-16-8","C10H18O",None,1165,None,1165),
("Terpineol <β->","7299-40-3","C10H18O",None,1159,None,1159),
("Terpineol <γ->","586-81-2","C10H18O",None,1199,None,1199),
("Terpineol <δ->","7299-42-5","C10H18O",None,1162,None,1162),
("Terpineol <1->","586-82-3","C10H18O",None,1130,None,1130),
("Menth-2-en-1-ol <cis-p->","29803-82-5","C10H18O",None,1118,None,1118),
("Menth-2-en-1-ol <trans-p->","29803-81-4","C10H18O",None,1136,None,1136),
("Menth-3-en-8-ol <p->","24302-23-6","C10H18O",None,1145,None,1145),
("Menth-1-en-9-ol <p->","18479-68-0","C10H18O",None,1294,None,1294),
("Carveol <cis->","1197-06-4","C10H16O",None,1226,None,1226),
("Carveol <trans->","1197-07-5","C10H16O",None,1215,None,1215),
("Dihydro carveol","38049-26-2","C10H18O",None,1192,None,1192),
("Dihydro carveol <iso->","18675-35-9","C10H18O",None,1212,None,1212),
("Dihydro carveol <neo->","18675-33-7","C10H18O",None,1193,None,1193),
("Dihydro carveol <neoiso->","18675-34-8","C10H18O",None,1226,None,1226),
("Pulegol <cis->","22472-80-6","C10H18O",None,1226,None,1226),
("Pulegol <trans->","22472-79-3","C10H18O",None,1213,None,1213),
("Isopulegol","121468-66-4","C10H18O",None,1145,None,1145),
("Isopulegol <iso->","59905-54-3","C10H18O",None,1155,None,1155),
("Isopulegol <neo->","59905-53-2","C10H18O",None,1144,None,1144),
("Isopulegol <neoiso->","21290-09-5","C10H18O",None,1167,None,1167),
("Piperitol <cis->","34350-53-3","C10H18O",None,1195,None,1195),
("Piperitol <trans->","16721-39-4","C10H18O",None,1207,None,1207),
("Perilla alcohol","536-59-4","C10H16O",None,1294,None,1294),
("Thujanol <3->","3284-85-3","C10H18O",None,1164,None,1164),
("Thujanol <iso-3->","7712-79-0","C10H18O",None,1134,None,1134),
("Thujanol <neo-3->","21653-18-9","C10H18O",None,1149,None,1149),
("Thujanol <neoiso-3->","21653-19-0","C10H18O",None,1147,None,1147),
("Verbanol","515-88-8","C10H18O",None,1197,None,1197),
("Verbanol <iso->","473-65-4","C10H18O",None,1176,None,1176),
("Verbanol <neo->","94480-82-7","C10H18O",None,1182,None,1182),
("Verbanol <neoiso->","94480-81-6","C10H18O",None,1187,None,1187),
("Pinocampheol","25465-95-6","C10H18O",None,1166,None,1166),
("Myrtanol <cis->","15358-92-6","C10H18O",None,1250,None,1250),
("Myrtanol <trans->","15358-91-5","C10H18O",None,1258,None,1258),
("Nopol","128-50-7","C11H18O",None,1278,None,1278),
("Nerol oxide","1786-08-9","C10H16O",None,1154,None,1154),
("Rose oxide <cis->","4610-11-1","C10H18O",None,1106,None,1106),
("Rose oxide <trans->","5258-11-7","C10H18O",None,1122,None,1122),
("Linalool oxide <cis-> (furanoid)","5989-33-3","C10H18O2",None,1067,None,1067),
("Linalool oxide <trans-> (furanoid)","34995-77-2","C10H18O2",None,1084,None,1084),
("Linalool oxide <cis-> (pyranoid)","14009-71-3","C10H18O2",None,1170,None,1170),
("Linalool oxide <trans-> (pyranoid)","41720-62-1","C10H18O2",None,1173,None,1173),

# Additional monoterpene ketones
("Fenchone","1195-79-5","C10H16O",None,1083,None,1083),
("Menthone <iso->","491-07-6","C10H18O",None,1158,None,1158),
("Pulegone","89-82-7","C10H16O",None,1233,None,1233),
("Piperitone","89-81-6","C10H16O",None,1249,None,1249),
("Piperitenone","491-09-8","C10H14O",None,1340,None,1340),
("Carvone","99-49-0","C10H14O",None,1239,None,1239),
("Dihydro carvone <cis->","7764-50-3","C10H16O",None,1191,None,1191),
("Dihydro carvone <trans->","5948-04-9","C10H16O",None,1200,None,1200),
("Carvotanacetone","499-71-8","C10H16O",None,1244,None,1244),
("Carvone oxide <cis->","18383-49-8","C10H14O2",None,1259,None,1259),
("Carvone oxide <trans->","39903-97-4","C10H14O2",None,1273,None,1273),
("Carvone hydrate","7712-46-1","C10H16O2",None,1422,None,1422),
("Pinocarvone","16812-40-1","C10H14O",None,1160,None,1160),
("Pinocamphone <cis->","15358-88-0","C10H16O",None,1172,None,1172),
("Pinocamphone <trans->","547-60-4","C10H16O",None,1158,None,1158),
("Nopinone","38651-65-9","C9H14O",None,1135,None,1135),
("Camphenilone","13211-15-9","C9H14O",None,1078,None,1078),
("Chrysanthenone","473-06-3","C10H14O",None,1124,None,1124),
("Umbellulone","24545-81-1","C10H14O",None,1167,None,1167),
("Cryptone","500-02-7","C9H14O",None,1183,None,1183),
("Menthofuran","494-90-6","C10H14O",None,1159,None,1159),
("Eucarvone","503-93-5","C10H14O",None,1146,None,1146),
("Karahanaenone","19822-67-4","C10H16O",None,1154,None,1154),
("Sabina ketone","513-20-2","C9H14O",None,1154,None,1154),
("Isophorone","78-59-1","C9H14O",None,1118,None,1118),
("Dihydroisojasmone","1128-08-1","C11H18O",None,1340,None,1340),
("Jasmone <(E)->","6261-18-3","C11H16O",None,1390,None,1390),
("Jasmone <dihydro->","1128-08-1","C11H18O",None,1378,None,1378),
("Methyl dihydro jasmonate <trans->","2630-39-9","C13H22O3",None,1682,None,1682),

# Additional monoterpene esters
("Linalool acetate <dihydro->","108597-90-6","C12H22O2",None,1272,None,1272),
("Linalool acetate <tetrahydro->","20780-48-7","C12H24O2",None,1231,None,1231),
("Linalool formate","115-99-1","C11H18O2",None,1214,None,1214),
("Linalool propanoate","144-39-8","C13H22O2",None,1334,None,1334),
("Linalool butanoate","78-36-4","C14H24O2",None,1421,None,1421),
("Linalool isobutanoate","78-35-3","C14H24O2",None,1373,None,1373),
("Linalool isovalerate","1118-27-0","C15H26O2",None,1466,None,1466),
("Isobornyl acetate","125-12-2","C12H20O2",None,1283,None,1283),
("Isobornyl formate","1200-67-5","C11H18O2",None,1235,None,1235),
("Isobornyl propanoate","2756-56-1","C13H22O2",None,1383,None,1383),
("Isobornyl n-butanoate","107910-89-4","C14H24O2",None,1473,None,1473),
("Isobornyl isobutanoate","107910-88-3","C14H24O2",None,1431,None,1431),
("Isobornyl isovalerate","7779-73-9","C15H26O2",None,1521,None,1521),
("Bornyl angelate","85758-37-8","C15H24O2",None,1564,None,1564),
("Fenchyl acetate <endo->","4057-31-2","C12H20O2",None,1218,None,1218),
("Fenchyl acetate <exo->","56282-46-3","C12H20O2",None,1229,None,1229),
("Terpinyl isobutanoate <α->","7774-65-4","C14H24O2",None,1471,None,1471),
("Geranyl formate","105-86-2","C11H18O2",None,1298,None,1298),
("Geranyl propanoate","105-90-8","C13H22O2",None,1476,None,1476),
("Geranyl butanoate","106-29-6","C14H24O2",None,1562,None,1562),
("Geranyl isobutanoate","2345-26-8","C14H24O2",None,1514,None,1514),
("Geranyl isovalerate","109-20-6","C15H26O2",None,1606,None,1606),
("Geranyl tiglate","7785-33-3","C15H24O2",None,1696,None,1696),
("Geranyl valerate","10402-47-8","C15H26O2",None,1655,None,1655),
("Geranyl 2-methyl butanoate","68705-63-5","C15H26O2",None,1601,None,1601),
("Geranyl benzoate","94-84-4","C17H22O2",None,1958,None,1958),
("Neryl formate","2142-94-1","C11H18O2",None,1280,None,1280),
("Neryl propanoate","105-91-9","C13H22O2",None,1452,None,1452),
("Neryl isobutanoate","2345-24-6","C14H24O2",None,1490,None,1490),
("Neryl isovalerate","3915-83-1","C15H26O2",None,1582,None,1582),
("Nerolidyl acetate <(E)->","85611-33-2","C17H28O2",None,1716,None,1716),
("Nerolidyl acetate <(Z)->","91050-14-5","C17H28O2",None,1676,None,1676),
("Citronellyl acetate","150-84-5","C12H22O2",None,1352,None,1352),
("Citronellyl formate","105-85-1","C11H20O2",None,1273,None,1273),
("Citronellyl propanoate","141-14-0","C13H24O2",None,1444,None,1444),
("Citronellyl butanoate","141-16-2","C14H26O2",None,1530,None,1530),
("Citronellyl isobutanoate","97-89-2","C14H26O2",None,1482,None,1482),
("Citronellyl pentanoate","7540-53-6","C15H28O2",None,1624,None,1624),
("Citronellyl tiglate","24717-85-9","C15H26O2",None,1666,None,1666),
("Citronellyl oxy-acetaldehyde","7492-67-3","C12H22O2",None,1409,None,1409),
("Citronellyl anthranilate","68555-57-7","C17H25NO2",None,2180,None,2180),
("Lavandulyl acetate","20777-39-3","C12H20O2",None,1288,None,1288),
("Lavandulyl isobutanoate","51117-20-5","C14H24O2",None,1421,None,1421),
("Lavandulyl isovalerate","51117-21-6","C15H26O2",None,1509,None,1509),
("Menthyl acetate","89-48-5","C12H22O2",None,1294,None,1294),
("Menthyl acetate <iso->","20777-45-1","C12H22O2",None,1304,None,1304),
("Menthyl acetate <neo->","2230-87-7","C12H22O2",None,1271,None,1271),
("Menthyl isovalerate","28221-20-7","C15H28O2",None,1516,None,1516),
("Menthyl lactate","59259-38-0","C13H24O3",None,1481,None,1481),
("Carvyl acetate <cis->","1205-42-1","C12H18O2",None,1365,None,1365),
("Carvyl acetate <trans->","1134-95-8","C12H18O2",None,1339,None,1339),
("Carvyl propanoate <cis->","145032-50-4","C13H20O2",None,1420,None,1420),
("Carvyl propanoate <trans->","74431-24-6","C13H20O2",None,1454,None,1454),
("Dihydro carveol acetate","75684-65-0","C12H20O2",None,1306,None,1306),
("Dihydro carveol acetate <iso->","160868-58-6","C12H20O2",None,1326,None,1326),
("Dihydro carveol acetate <neo->","75684-64-9","C12H20O2",None,1306,None,1306),
("Dihydro carveol acetate <neoiso->","256332-36-2","C12H20O2",None,1356,None,1356),
("Dihydro citronellol acetate","20780-49-8","C12H24O2",None,1319,None,1319),
("Dihydro myrcenol acetate","53767-93-4","C12H22O2",None,1214,None,1214),
("Myrtenyl acetate","1079-01-2","C12H18O2",None,1324,None,1324),
("Myrtanol acetate <trans->","90934-53-5","C12H20O2",None,1385,None,1385),
("Pinocarvyl acetate <cis->","73366-18-4","C12H18O2",None,1311,None,1311),
("Pinocarvyl acetate <trans->","1686-15-3","C12H18O2",None,1298,None,1298),
("Verbenyl acetate <cis->","29135-27-1","C12H18O2",None,1280,None,1280),
("Verbenyl acetate <trans->","1203-21-0","C12H18O2",None,1291,None,1291),
("Sabinyl acetate <trans->","53833-85-5","C12H18O2",None,1289,None,1289),
("Thujanol acetate <3->","72747-24-1","C12H20O2",None,1295,None,1295),
("Thujanol acetate <iso-3->","62181-90-2","C12H20O2",None,1267,None,1267),
("Thujanol acetate <neo-3->","370557-87-2","C12H20O2",None,1273,None,1273),
("Thujanol acetate <neoiso-3->","62181-91-3","C12H20O2",None,1281,None,1281),
("Sabinene hydrate acetate <cis->","77318-48-0","C12H20O2",None,1219,None,1219),
("Sabinene hydrate acetate <trans->","77318-47-9","C12H20O2",None,1253,None,1253),
("Isopulegyl acetate","109010-12-0","C12H20O2",None,1275,None,1275),
("Piperitol acetate <cis->","112028-22-5","C12H20O2",None,1332,None,1332),
("Piperitol acetate <trans->","91159-15-8","C12H20O2",None,1343,None,1343),
("Carvomenthyl acetate <neoiso->","20777-43-9","C12H22O2",None,1347,None,1347),
("Cymen-7-ol acetate <p->","59230-57-8","C12H16O2",None,1421,None,1421),
("Menth-1-en-9-ol acetate <p->","28839-13-6","C12H20O2",None,1421,None,1421),
("Terpinen-4-ol acetate","4821-04-9","C12H20O2",None,1299,None,1299),
("Nopyl acetate","128-51-8","C13H20O2",None,1424,None,1424),
("Methyl myrtenate","30649-97-9","C11H16O2",None,1293,None,1293),
("Methyl thujate","54598-10-6","C11H14O2",None,1318,None,1318),
("Methyl perillate","54298-90-7","C11H16O2",None,1392,None,1392),
("Methyl citronellate","2270-60-2","C11H20O2",None,1257,None,1257),
("Methyl geranate","2349-14-6","C11H18O2",None,1322,None,1322),
("Methyl nerolate","1862-61-9","C11H18O2",None,1280,None,1280),
("Ethyl nerolate","32659-20-4","C12H20O2",None,1351,None,1351),
("Ethyl geranate","32659-21-5","C12H20O2",None,1394,None,1394),

# Additional phenolic / aromatic
("Anethole <(Z)->","25679-28-1","C10H12O",None,1249,None,1249),
("Eugenol acetate","93-28-7","C12H14O3",None,1521,None,1521),
("Eugenol <dihydro->","2785-87-7","C10H14O2",None,1366,None,1366),
("Isoeugenol <(E)->","5932-68-3","C10H12O2",None,1451,None,1451),
("Isoeugenol <(Z)->","5912-86-7","C10H12O2",None,1406,None,1406),
("Methyl isoeugenol <(E)->","6379-72-2","C11H14O2",None,1492,None,1492),
("Methyl isoeugenol <(Z)->","6380-24-1","C11H14O2",None,1453,None,1453),
("Chavicol","501-92-8","C9H10O",None,1250,None,1250),
("Chavibetol acetate","1941-09-9","C12H14O3",None,1524,None,1524),
("Cinnamaldehyde <(Z)->","57194-69-1","C9H8O",None,1217,None,1217),
("Cinnamaldehyde <α-methyl->","101-39-3","C10H10O",None,1318,None,1318),
("Cinnamaldehyde <hydro->","104-53-0","C9H10O",None,1599,None,1599),
("Cinnamaldehyde <4-hydroxy-3-methoxy->","20649-42-7","C10H10O3",None,1728,None,1728),
("Cinnamaldehyde <(E)-p-methoxy->","24680-50-0","C10H10O2",None,1564,None,1564),
("Methoxy cinnamaldehyde <(E)-o->","60125-24-8","C10H10O2",None,1527,None,1527),
("Methoxy cinnamic acid <(4E)->","943-89-5","C10H10O3",None,1700,None,1700),
("Cinnamic acid <(E)->","140-10-3","C9H8O2",None,1452,None,1452),
("Benzyl formate","104-57-4","C8H8O2",None,1071,None,1071),
("Benzyl propanoate","122-63-4","C10H12O2",None,1257,None,1257),
("Benzyl butanoate","103-37-7","C11H14O2",None,1343,None,1343),
("Benzyl isobutanoate","103-28-6","C11H14O2",None,1297,None,1297),
("Benzyl tiglate","37526-88-8","C12H14O2",None,1497,None,1497),
("Benzyl benzoate","120-51-4","C14H12O2",None,1759,None,1759),
("Benzyl salicylate","118-58-1","C14H12O3",None,1864,None,1864),
("Benzyl cinnamate","103-41-3","C16H14O2",None,2092,None,2092),
("Benzyl acetylacetate","5396-89-4","C11H12O3",None,1486,None,1486),
("Phenyl ethyl acetate <1->","93-92-5","C10H12O2",None,1192,None,1192),
("Phenyl ethyl formate <2->","104-62-1","C9H10O2",None,1172,None,1172),
("Phenyl ethyl propanoate <2->","122-70-3","C11H14O2",None,1351,None,1351),
("Phenyl ethyl butanoate <2->","103-52-6","C12H16O2",None,1439,None,1439),
("Phenyl ethyl isobutanoate","7775-39-5","C12H16O2",None,1393,None,1393),
("Phenyl ethyl 2-methylbutanoate","24817-51-4","C13H18O2",None,1486,None,1486),
("Phenyl ethyl 3-methyl butanoate","140-26-1","C13H18O2",None,1490,None,1490),
("Phenyl ethyl hexanoate","6290-37-5","C14H20O2",None,1642,None,1642),
("Phenyl ethyl octanoate","5457-70-5","C16H24O2",None,1846,None,1846),
("Phenyl ethyl tiglate <2->","55719-85-2","C13H16O2",None,1584,None,1584),
("Phenyl ethyl phenyl acetate <2->","102-20-5","C16H16O2",None,1913,None,1913),
("Phenyl ethyl anthranilate <2->","133-18-6","C15H15NO2",None,2126,None,2126),
("Phenyl ethyl oxyacetaldehyde","41847-88-5","C10H12O2",None,1324,None,1324),
("Phenethyl 2-furoate","7149-32-8","C13H12O3",None,1714,None,1714),
("Phenethyl cinnamate","103-53-7","C17H16O2",None,2179,None,2179),
("Ethyl salicylate","118-61-6","C9H10O3",None,1266,None,1266),
("Butyl salicylate","2052-14-4","C11H14O3",None,1469,None,1469),
("Hexyl salicylate","6259-76-3","C13H18O3",None,1674,None,1674),
("Isobutyl salicylate","87-19-4","C11H14O3",None,1423,None,1423),
("Isopentyl salicylate","87-20-7","C12H16O3",None,1535,None,1535),
("Pentyl salicylate","2050-08-0","C12H16O3",None,1574,None,1574),
("Salicylaldehyde","90-02-8","C7H6O2",None,1039,None,1039),
("Vanillin <ethyl->","121-32-4","C9H10O3",None,1452,None,1452),
("Vanillin <o->","148-53-8","C8H8O3",None,1302,None,1302),
("Vanillin acetate","881-68-5","C10H10O4",None,1525,None,1525),
("Vanillone, aceto-","498-02-2","C9H10O3",None,1481,None,1481),
("Vanillyl alcohol","498-00-0","C8H10O3",None,1445,None,1445),
("Methyl vanillin","120-14-9","C9H10O3",None,1475,None,1475),
("Syringaldehyde","134-96-3","C9H10O4",None,1655,None,1655),
("Syringol","91-10-1","C8H10O3",None,1346,None,1346),
("Cresol <o->","95-48-7","C7H8O",None,1050,None,1050),
("Cresol <m->","108-39-4","C7H8O",None,1072,None,1072),
("Cresol <p->","106-44-5","C7H8O",None,1071,None,1071),
("Cresol methyl ether <o->","578-58-5","C8H10O",None,1005,None,1005),
("Cresol acetate <o->","533-18-6","C9H10O2",None,1134,None,1134),
("Cresol acetate <m->","122-46-3","C9H10O2",None,1158,None,1158),
("Cresol acetate <p->","140-39-6","C9H10O2",None,1166,None,1166),
("Cresol <2-methoxy-p->","93-51-6","C8H10O2",None,1188,None,1188),
("Cresol isobutyrate <p->","103-93-5","C11H14O2",None,1305,None,1305),
("Guaiacol <o->","90-05-1","C7H8O2",None,1089,None,1089),
("Guaiacol <p-vinyl->","7786-61-0","C9H10O2",None,1309,None,1309),
("Guaiacol acetate <o->","613-70-7","C9H10O3",None,1265,None,1265),
("Methyoxythiophenol <2->","7217-59-6","C7H8OS",None,1211,None,1211),
("Anisaldehyde <p->","123-11-5","C8H8O2",None,1247,None,1247),
("Anisaldehyde <o->","135-02-4","C8H8O2",None,1239,None,1239),
("Anisaldehyde, <meta->","591-31-1","C8H8O2",None,1195,None,1195),
("Anisyl alcohol <p->","105-13-5","C8H10O2",None,1278,None,1278),
("Anisyl alcohol <meta->","6971-51-3","C8H10O2",None,1280,None,1280),
("Anisyl acetate <p->","1331-83-5","C10H12O3",None,1412,None,1412),
("Anisyl formate","122-91-8","C9H10O3",None,1330,None,1330),
("Anisyl propanoate","7549-33-9","C11H14O3",None,1511,None,1511),
("Anisyl methyl ketone","122-84-9","C10H12O2",None,1382,None,1382),
("Anisole","100-66-3","C7H8O",None,913,None,913),
("Anisole <p-methyl->","104-93-8","C8H10O",None,1015,None,1015),
("Acetophenone","98-86-2","C8H8O",None,1059,None,1059),
("Acetophenone <p-methyl->","122-00-9","C9H10O",None,1179,None,1179),
("Acetophenone <3'-methoxy->","586-37-8","C9H10O2",None,1298,None,1298),
("Acetophenone <4'-methoxy->","100-06-1","C9H10O2",None,1347,None,1347),
("Acetanisole <o->","579-74-8","C9H10O2",None,1290,None,1290),
("Ethyl acetophenone <p->","937-30-4","C10H12O",None,1279,None,1279),
("Hydroxy acetophenone <2'->","118-93-4","C8H8O2",None,1155,None,1155),
("Hydroxybenzaldehyde <4->","123-08-0","C7H6O2",None,1355,None,1355),
("Benzenemethanol <2-hydroxy->","90-01-7","C7H8O2",None,1255,None,1255),
("Benzene methanol <α-methyl->","98-85-1","C8H10O",None,1057,None,1057),
("Phenyl propanal <2->","93-53-8","C9H10O",None,1102,None,1102),
("Hydrocinnamyl alcohol","122-97-4","C9H12O",None,1224,None,1224),
("Hydrocinnamyl acetate","122-72-5","C11H14O2",None,1368,None,1368),
("Cyclamen aldehyde","103-95-7","C13H18O",None,1459,None,1459),
("Lilial","80-54-6","C14H20O",None,1528,None,1528),
("Methyl benzoate","93-58-3","C8H8O2",None,1088,None,1088),
("Ethyl benzoate","93-89-0","C9H10O2",None,1169,None,1169),
("Methyl cinnamate <(E)->","1754-62-7","C10H10O2",None,1376,None,1376),
("Methyl cinnamate <(Z)->","19713-73-6","C10H10O2",None,1299,None,1299),
("Ethyl cinnamate <(E)->","4192-77-2","C11H12O2",None,1465,None,1465),
("Ethyl cinnamate <(Z)->","4610-69-9","C11H12O2",None,1376,None,1376),
("Cinnamyl alcohol <(E)->","4407-36-7","C9H10O",None,1303,None,1303),
("Cinnamyl alcohol <(Z)->","4510-34-3","C9H10O",None,1259,None,1259),
("Cinnamyl acetate <(E)->","21040-45-9","C11H12O2",None,1443,None,1443),
("Cinnamyl acetate <(Z)->","77134-01-1","C11H12O2",None,1388,None,1388),
("Benzoin","579-44-2","C14H12O2",None,1803,None,1803),
("Benzophenone","119-61-9","C13H10O",None,1626,None,1626),
("Benzofuran <2,3-dimethyl->","3782-00-1","C10H10O",None,1221,None,1221),
("Benzene <pentyl->","538-68-1","C11H16",None,1156,None,1156),
("Benzene <1,3-dimethoxy->","151-10-0","C8H10O2",None,1168,None,1168),
("Benzaldehyde, dimethyl acetal","1125-88-8","C9H12O2",None,1111,None,1111),
("Dimethoxybenzene <1,4->","150-78-7","C8H10O2",None,1165,None,1165),
("Dimethyl phenol <2,6->","576-26-1","C8H10O",None,1107,None,1107),
("Orcinol","504-15-4","C7H8O2",None,1370,None,1370),
("Catechol <3-methyl->","488-17-5","C7H8O2",None,1258,None,1258),
("Phenol <2-allyl->","1745-81-9","C9H10O",None,1189,None,1189),
("Phenol <2-(1E)-propenyl->","23619-59-2","C9H10O",None,1264,None,1264),
("Phenol <2-(1Z)-propenyl->","23508-99-8","C9H10O",None,1146,None,1146),
("Phenol <2,6-dimethoxy->","91-10-1","C8H10O3",None,1346,None,1346),
("Indole","120-72-9","C8H7N",None,1291,None,1291),
("Skatole","83-34-1","C9H9N",None,1383,None,1383),
("Isoquinoline","119-65-3","C9H7N",None,1253,None,1253),
("Nicotine","54-11-5","C10H14N2",None,1345,None,1345),
("Biphenyl","92-52-4","C12H10",None,1377,None,1377),
("Methyl biphenyl <4->","644-08-6","C13H12",None,1489,None,1489),
("Naphthalene","91-20-3","C10H8",None,1181,None,1181),
("Naphthalene <1-methoxy->","2216-69-5","C11H10O",None,1446,None,1446),
("Naphthalene <2-methoxy->","93-04-9","C11H10O",None,1447,None,1447),
("Azulene","275-51-4","C10H8",None,1298,None,1298),
("Guaiazulene","489-84-9","C15H18",None,1779,None,1779),

# Additional sesquiterpene hydrocarbons
("α-Cadinene","82468-90-4","C15H24",None,1537,None,1537),
("Cadina-1(6),4-diene <cis->","246522-85-0","C15H24",None,1461,None,1461),
("Cadina-1(6),4-diene <trans->","20085-11-4","C15H24",None,1475,None,1475),
("Cadina-1,4-diene <cis->","29837-12-5","C15H24",None,1495,None,1495),
("Cadina-1,4-diene <trans->","38758-02-0","C15H24",None,1533,None,1533),
("Cedrene <α->","469-61-4","C15H24",None,1410,None,1410),
("Cedrene <β->","546-28-1","C15H24",None,1419,None,1419),
("Cedrane","13567-55-0","C15H26",None,1441,None,1441),
("Cuprenene <α->","29621-78-1","C15H24",None,1505,None,1505),
("Cyclosativene","22469-52-9","C15H24",None,1369,None,1369),
("Daucene","16661-00-0","C15H24",None,1380,None,1380),
("Germacrene A","28387-44-2","C15H24",None,1508,None,1508),
("Germacrene B","15423-57-1","C15H24",None,1559,None,1559),
("Gurjunene <β->","17334-55-3","C15H24",None,1431,None,1431),
("Gurjunene <γ->","22567-17-5","C15H24",None,1475,None,1475),
("Himachalene <α->","3853-83-6","C15H24",None,1449,None,1449),
("Himachalene <β->","1461-03-6","C15H24",None,1500,None,1500),
("Himachalene <γ->","53111-25-4","C15H24",None,1481,None,1481),
("Humulene <β->","116-04-1","C15H24",None,1436,None,1436),
("Ishwarane","26620-70-2","C15H24",None,1465,None,1465),
("Isocomene <α->","65372-78-3","C15H24",None,1387,None,1387),
("Isocomene <β->","71596-72-0","C15H24",None,1407,None,1407),
("Isoledene","95910-36-4","C15H24",None,1374,None,1374),
("Italicene","94535-52-1","C15H24",None,1405,None,1405),
("Khusimene","18444-94-5","C15H24",None,1453,None,1453),
("Ledene","21747-46-6","C15H24",None,1496,None,1496),
("Longicyclene","1137-12-8","C15H24",None,1371,None,1371),
("Longifolene","475-20-7","C15H24",None,1407,None,1407),
("Longipinene <β->","41432-70-6","C15H24",None,1400,None,1400),
("Modheph-2-ene","68269-87-4","C15H24",None,1382,None,1382),
("Muurola-3,5-diene <cis->","157374-44-2","C15H24",None,1448,None,1448),
("Muurola-3,5-diene <trans->","189165-77-3","C15H24",None,1451,None,1451),
("Nootkatene","5090-61-9","C15H22",None,1517,None,1517),
("Occidentalol","473-17-6","C15H24O",None,1550,None,1550),
("Panasinsene <β->","56684-97-0","C15H24",None,1381,None,1381),
("Prezizaene","116498-31-8","C15H24",None,1444,None,1444),
("Pseudowiddrene","32540-28-6","C15H24",None,1498,None,1498),
("Rotundene","65128-08-7","C15H24",None,1457,None,1457),
("Sativene","6813-05-4","C15H24",None,1390,None,1390),
("Sesquithujene","58319-06-5","C15H24",None,1405,None,1405),
("Seychellene","20085-93-2","C15H24",None,1444,None,1444),
("Silphiperfol-5-ene","138752-24-6","C15H24",None,1326,None,1326),
("Silphiperfol-6-ene","74284-56-3","C15H24",None,1377,None,1377),
("Silphinene","74284-57-4","C15H24",None,1345,None,1345),
("Thujopsene <cis->","470-40-6","C15H24",None,1429,None,1429),
("Thujopsadiene <cis->","51446-91-4","C15H24",None,1465,None,1465),
("Vetispirene <α->","51196-11-3","C15H22",None,1489,None,1489),
("Vetispirene <β->","28908-27-2","C15H22",None,1493,None,1493),
("Vetivenene <β->","27840-40-0","C15H22",None,1554,None,1554),
("Vetivenene <γ->","28908-26-1","C15H22",None,1531,None,1531),
("Viridiflorene","21747-46-6","C15H24",None,1496,None,1496),
("Zierone","6754-66-1","C15H22O",None,1574,None,1574),
("Zonarene","41929-05-9","C15H24",None,1528,None,1528),

# Additional sesquiterpene alcohols
("Cedrol <epi->","19903-73-2","C15H26O",None,1618,None,1618),
("Cubenol <1-epi->","19912-67-5","C15H26O",None,1627,None,1627),
("τ-Cadinol","5937-11-1","C15H26O",None,1638,None,1638),
("τ-Muurolol","19912-62-0","C15H26O",None,1640,None,1640),
("α-Muurolol","19435-97-3","C15H26O",None,1644,None,1644),
("epi-α-Bisabolol","23178-88-3","C15H26O",None,1683,None,1683),
("epi-β-Bisabolol","235421-59-7","C15H26O",None,1670,None,1670),
("Farnesol <2,3-dihydro->","27745-36-4","C15H28O",None,1688,None,1688),
("Nootkatol <epi->","50763-66-1","C15H24O",None,1699,None,1699),
("β-Acorenol","28400-11-5","C15H26O",None,1636,None,1636),
("Acorenone","5956-05-8","C15H24O",None,1692,None,1692),
("Eudesmol <dihydro->","6770-16-7","C15H28O",None,1661,None,1661),
("Eudesm-7(11)-en-4-ol","473-04-1","C15H26O",None,1700,None,1700),
("Longiborneol","465-24-7","C15H26O",None,1599,None,1599),
("Hinesol acetate","88494-77-3","C17H28O2",None,1783,None,1783),
("Valerianol","20489-45-6","C15H26O",None,1658,None,1658),
("Agarospirol","1460-73-7","C15H26O",None,1646,None,1646),
("Pogostol","21698-41-9","C15H26O",None,1651,None,1651),
("Norpatchoulenol","41429-52-1","C14H22O",None,1553,None,1553),
("Santalol <(Z)-β->","77-42-9","C15H24O",None,1715,None,1715),
("Santalol <(E)-β->","37172-32-0","C15H24O",None,1738,None,1738),
("Santalol acetate <(Z)-α->","41414-75-9","C17H26O2",None,1777,None,1777),
("Santalol acetate <(Z)-β->","77-43-0","C17H26O2",None,1818,None,1818),
("Santalol acetate <(E)-β->","78856-39-0","C17H26O2",None,1867,None,1867),
("Bergamotol <(Z)-α-trans->","88034-74-6","C15H24O",None,1690,None,1690),
("Bergamotol acetate <(Z)-α-trans->","87978-33-4","C17H26O2",None,1794,None,1794),
("Lanceol <(Z)->","10067-28-4","C15H24O",None,1760,None,1760),
("Lanceol acetate <(Z)->","117898-00-7","C17H26O2",None,1854,None,1854),
("Nuciferol <(Z)->","78339-53-4","C15H22O",None,1724,None,1724),
("Nuciferol <(E)->","39599-18-3","C15H22O",None,1754,None,1754),
("Nuciferal <(Z)->","122442-35-7","C15H20O",None,1713,None,1713),
("Nuciferal <(E)->","25532-74-5","C15H20O",None,1727,None,1727),
("Nootkatin","4431-03-2","C15H20O2",None,1959,None,1959),
("Nootkatinol","2492-08-2","C15H22O3",None,2088,None,2088),
("Elemicin","487-11-6","C12H16O3",None,1555,None,1555),
("Isoelemicin <(E)->","5273-85-8","C12H16O3",None,1568,None,1568),
("Isoelemicin <(Z)->","5273-84-7","C12H16O3",None,1568,None,1568),
("Myristicin","607-91-0","C11H12O3",None,1517,None,1517),
("Apiole","523-80-8","C12H14O4",None,1677,None,1677),
("Dill apiole","484-31-1","C12H14O4",None,1620,None,1620),
("Safrole","94-59-7","C10H10O2",None,1285,None,1285),
("Isosafrole <(E)->","4043-71-4","C10H10O2",None,1373,None,1373),
("Isosafrole <(Z)->","17627-76-8","C10H10O2",None,1336,None,1336),
("Asarone <(E)->","2883-98-9","C12H16O3",None,1675,None,1675),
("Asarone <(Z)->","5273-86-9","C12H16O3",None,1616,None,1616),
("Asarone <γ->","5353-15-1","C12H16O3",None,1572,None,1572),
("Croweacin","484-34-4","C11H12O3",None,1457,None,1457),
("Asaricin","18607-93-7","C11H12O3",None,1495,None,1495),

# Additional diterpenes
("Manool <13-epi->","1438-62-6","C20H34O",None,2059,None,2059),
("Manool oxide <13-epi->","1227-93-6","C20H34O",None,2009,None,2009),
("Isophytol","505-32-8","C20H40O",None,1946,None,1946),
("Geranyl linalool <(E,E)->","1113-21-9","C20H34O",None,2026,None,2026),
("Pimaradiene","1686-61-9","C20H32",None,1948,None,1948),
("Sandaracopimara-8(14),15-diene","1686-56-2","C20H32",None,1968,None,1968),
("Sandaracopimarinol","24563-84-6","C20H32O",None,2269,None,2269),
("Sandaracopimarinal","3855-14-9","C20H30O",None,2184,None,2184),
("Isopimarol","1686-64-2","C20H32O",None,2310,None,2310),
("Methyl isopimarate","1686-62-0","C21H32O2",None,2297,None,2297),
("Methyl pimarate","3730-56-1","C21H32O2",None,2237,None,2237),
("Methyl sandaracopimarate","1686-54-0","C21H32O2",None,2256,None,2256),
("Methyl dehydroabietate","1235-74-1","C21H30O2",None,2341,None,2341),
("Methyl abietate","127-25-3","C21H32O2",None,2385,None,2385),
("Methyl neoabietate","3310-97-2","C21H32O2",None,2443,None,2443),
("Methyl levopimarate","3513-69-7","C21H32O2",None,2306,None,2306),
("Abietal","6704-50-3","C20H30O",None,2313,None,2313),
("Abietal <4-epi->","34223-60-4","C20H30O",None,2298,None,2298),
("Abietal <dehydro->","13601-88-2","C20H28O",None,2274,None,2274),
("Abietatriene","19407-28-4","C20H30",None,2055,None,2055),
("Abietadien-18-ol","21414-53-9","C20H32O",None,2324,None,2324),
("Abietol","666-84-2","C20H32O",None,2401,None,2401),
("Abietol <4-epi->","24563-94-8","C20H32O",None,2343,None,2343),
("Abietol <neo->","640-42-6","C20H32O",None,2468,None,2468),
("Abietol, dehydro","3772-55-2","C20H30O",None,2368,None,2368),
("Abienol","1616-86-0","C20H34O",None,2149,None,2149),
("Ferruginol <trans->","514-62-5","C20H30O",None,2331,None,2331),
("Ferruginol <6,7-dehydro->","34539-84-9","C20H28O",None,2315,None,2315),
("Ferruginol <6-keto->","70614-89-0","C20H28O2",None,2456,None,2456),
("Ferruginol acetate <trans->","15340-79-1","C22H32O2",None,2363,None,2363),
("Totarol <trans->","511-15-9","C20H30O",None,2314,None,2314),
("Totarol acetate <trans->","15340-82-6","C22H32O2",None,2428,None,2428),
("Totarolone","6755-93-7","C20H28O2",None,2542,None,2542),
("Hinokiol","564-73-8","C20H30O2",None,2589,None,2589),
("Hinokione","472-37-7","C20H28O2",None,2549,None,2549),
("Hinokienone","18326-19-7","C20H26O2",None,2557,None,2557),
("Sugiol","511-05-7","C20H28O2",None,2629,None,2629),
("Sempervirol","1857-11-0","C20H30O",None,2282,None,2282),
("Sclarene","511-02-4","C20H32",None,1974,None,1974),
("Rimuene","1686-67-5","C20H32",None,1896,None,1896),
("Beyerene","2359-73-1","C20H32",None,1931,None,1931),
("Isohibaene","5975-53-1","C20H32",None,1933,None,1933),
("Kaur-15-ene","5947-50-2","C20H32",None,1997,None,1997),
("Kaurene","34424-57-2","C20H32",None,2043,None,2043),
("Isophyllocladene","511-85-3","C20H32",None,1966,None,1966),
("Phyllocladene","20070-61-5","C20H32",None,2016,None,2016),
("Cembrene","1898-13-1","C20H32",None,1937,None,1937),
("Cembrene A <(3E)->","31570-39-5","C20H32",None,1947,None,1947),
("Dolabradiene","3650-13-3","C20H32",None,1973,None,1973),
("Cubitene","66723-19-1","C20H32",None,1878,None,1878),
("Laurenene","90025-15-3","C20H32",None,1879,None,1879),
("Rosa-5,15-diene <ent->","78821-30-4","C20H32",None,1933,None,1933),
("Incensole","22419-74-5","C20H34O2",None,2158,None,2158),
("Incensole acetate","34701-53-6","C22H36O3",None,2184,None,2184),
("Incensole oxide","21698-66-8","C20H34O3",None,2279,None,2279),
("Larixol","1438-66-0","C20H34O2",None,2265,None,2265),
("Torulosol","1908-44-7","C20H34O2",None,2360,None,2360),
("Methyl eperuate","13008-80-5","C21H36O2",None,2220,None,2220),
("Methyl communate <(Z)->","10178-35-5","C21H32O2",None,2231,None,2231),
("Methyl communate <(E)->","15798-13-7","C21H32O2",None,2257,None,2257),
("Methyl labdanolate","10267-25-1","C21H38O3",None,2381,None,2381),
("Communic acid","2761-77-5","C20H30O2",None,2365,None,2365),
("Methyl daniellate","1238-98-8","C21H30O3",None,2331,None,2331),
("Thujaplicin <α->","1946-74-3","C10H12O2",None,1410,None,1410),
("Thujaplicin <β->","499-44-5","C10H12O2",None,1475,None,1475),
("Thujaplicin <γ->","672-76-4","C10H12O2",None,1483,None,1483),

# Additional aliphatic / fatty acids
("Methyl linoleate","112-63-0","C19H34O2",None,2095,None,2095),
("Methyl oleate","112-62-9","C19H36O2",None,2100,None,2100),
("Methyl stearate","112-61-8","C19H38O2",None,2124,None,2124),
("Methyl palmitate","112-39-0","C17H34O2",None,1921,None,1921),
("Ethyl palmitate","628-97-7","C18H36O2",None,1992,None,1992),
("Ethyl stearate","111-61-5","C20H40O2",None,2196,None,2196),
("Isopropyl palmitate","142-91-6","C19H38O2",None,2024,None,2024),
("Ethyl myristate","124-06-1","C16H32O2",None,1796,None,1796),
("Methyl myristate","124-10-7","C15H30O2",None,1723,None,1723),
("Ethyl laurate","106-33-2","C14H28O2",None,1595,None,1595),
("Methyl laurate","111-82-0","C13H26O2",None,1525,None,1525),
("Ethyl decanoate","110-38-3","C12H24O2",None,1395,None,1395),
("Methyl decanoate","110-42-9","C11H22O2",None,1325,None,1325),
("Ethyl octanoate","106-32-1","C10H20O2",None,1197,None,1197),
("Methyl octanoate","111-11-5","C9H18O2",None,1127,None,1127),
("Ethyl hexanoate","123-66-0","C8H16O2",None,998,None,998),
("Methyl hexanoate","106-70-7","C7H14O2",None,927,None,927),
("Butyl butanoate","109-21-7","C8H16O2",None,994,None,994),
("Butyl acetate","123-86-4","C6H12O2",None,811,None,811),
("Butyl propanoate","590-01-2","C7H14O2",None,909,None,909),
("Propyl butanoate","105-66-8","C7H14O2",None,899,None,899),
("Ethyl butanoate","105-54-4","C6H12O2",None,802,None,802),
("Ethyl propanoate","105-37-3","C5H10O2",None,711,None,711),
("Methyl propanoate","554-12-1","C4H8O2",None,634,None,634),
("Ethyl acetate","141-78-6","C4H8O2",None,606,None,606),
("Hexyl acetate","142-92-7","C8H16O2",None,1009,None,1009),
("Hexyl butanoate","2639-63-6","C10H20O2",None,1192,None,1192),
("Hexyl hexanoate","6378-65-0","C12H24O2",None,1383,None,1383),
("Hexyl octanoate","1117-55-1","C14H28O2",None,1582,None,1582),
("Hexyl tiglate","16930-96-4","C11H20O2",None,1332,None,1332),
("Hexyl isobutanoate","2349-07-7","C10H20O2",None,1151,None,1151),
("Hexyl isovalerate","10032-13-0","C11H22O2",None,1244,None,1244),
("Hexyl propanoate","2445-76-3","C9H18O2",None,1101,None,1101),
("Pentyl butanoate","540-18-1","C9H18O2",None,1091,None,1091),
("Pentyl propanoate","624-54-4","C8H16O2",None,1007,None,1007),
("Isopentyl acetate","123-92-2","C7H14O2",None,876,None,876),
("Isopentyl isobutyrate","2050-01-3","C9H18O2",None,1009,None,1009),
("Isopentyl isovalerate","659-70-1","C10H20O2",None,1103,None,1103),
("Isopentyl butanoate","106-27-4","C9H18O2",None,1058,None,1058),
("Isoamyl propionate","105-68-0","C8H16O2",None,966,None,966),
("Isoamyl octanoate","2035-99-6","C13H26O2",None,1445,None,1445),
("Isoamyl benzoate","94-46-2","C12H16O2",None,1435,None,1435),
("Isoamyl 3-(2-furan)propionate","7779-67-1","C12H18O3",None,1431,None,1431),

# n-Alkanes
("Hexane <n->","110-54-3","C6H14",None,600,None,600),
("Heptane","142-82-5","C7H16",None,700,None,700),
("Octane <n->","111-65-9","C8H18",None,800,None,800),
("Nonane <n->","111-84-2","C9H20",None,900,None,900),
("Decane <n->","124-18-5","C10H22",None,1000,None,1000),
("Undecane <n->","1120-21-4","C11H24",None,1100,None,1100),
("Dodecane <n->","112-40-3","C12H26",None,1200,None,1200),
("Tridecane <n->","629-50-5","C13H28",None,1300,None,1300),
("Tetradecane <n->","629-59-4","C14H30",None,1400,None,1400),
("Pentadecane <n->","629-62-9","C15H32",None,1500,None,1500),
("Hexadecane <n->","544-76-3","C16H34",None,1600,None,1600),
("Heptadecane <n->","629-78-7","C17H36",None,1700,None,1700),
("Octadecane <n->","593-45-3","C18H38",None,1800,None,1800),
("Nonadecane <n->","629-92-5","C19H40",None,1900,None,1900),
("Eicosane <n->","112-95-8","C20H42",None,2000,None,2000),
("Heneicosane <n->","629-94-7","C21H44",None,2100,None,2100),
("Docosane <n->","629-97-0","C22H46",None,2200,None,2200),
("Tricosane <n->","638-67-5","C23H48",None,2300,None,2300),
("Tetracosane <n->","646-31-1","C24H50",None,2400,None,2400),
("Pentacosane <n->","629-99-2","C25H52",None,2500,None,2500),
("Hexacosane","630-01-3","C26H54",None,2600,None,2600),
("Heptacosane","593-49-7","C27H56",None,2700,None,2700),
("Octacosane","630-02-4","C28H58",None,2800,None,2800),
("Nonacosane","630-03-5","C29H60",None,2900,None,2900),
("Triacontane","638-68-6","C30H62",None,3000,None,3000),
("Untriacontane","630-04-6","C31H64",None,3100,None,3100),
("Dotriacontane","544-85-4","C32H66",None,3200,None,3200),
("Tritriacontane","630-05-7","C33H68",None,3300,None,3300),
("Tetratriacontane","14167-59-0","C34H70",None,3400,None,3400),

# Sulfur / Nitrogen compounds
("Thiazole","288-47-1","C3H3NS",None,732,None,732),
("Thiazole <4-methyl->","693-95-8","C4H5NS",None,814,None,814),
("Thiazole <2,4,5-trimethyl->","13623-11-5","C6H9NS",None,994,None,994),
("Thiazole <2-ethoxy->","15679-19-3","C5H7NOS",None,951,None,951),
("Thiazole <2-acetyl->","24295-03-2","C5H5NOS",None,1014,None,1014),
("Thiazole <2-isobutyl->","18640-74-9","C7H11NS",None,1030,None,1030),
("Isopropyl-4-methyl thiazole <2->","15679-13-7","C7H11NS",None,1012,None,1012),
("Pyrazine <methyl->","109-08-0","C5H6N2",None,819,None,819),
("Pyrazine <2-ethyl->","13925-00-3","C6H8N2",None,912,None,912),
("Pyrazine <2,3-dimethyl->","5910-89-4","C6H8N2",None,915,None,915),
("Pyrazine <2,5-dimethyl->","123-32-0","C6H8N2",None,908,None,908),
("Pyrazine <2,6-dimethyl->","108-50-9","C6H8N2",None,909,None,909),
("Pyrazine <2-ethyl-3-methyl->","15707-23-0","C7H10N2",None,1002,None,1002),
("Pyrazine <tetramethyl->","1124-11-4","C8H12N2",None,1083,None,1083),
("Pyrazine <2,3-diethyl->","15707-24-1","C8H12N2",None,1081,None,1081),
("Pyrazine <2-methoxy->","3149-28-8","C5H6N2O",None,896,None,896),
("Pyrazine <2-methoxy-3-methyl->","2847-30-5","C6H8N2O",None,967,None,967),
("Pyrazine <2-methoxy-3-(2-methylpropyl)->","24683-00-9","C9H14N2O",None,1179,None,1179),
("Pyrazine <2-acetyl->","22047-25-2","C6H6N2O",None,1017,None,1017),
("Pyrazine <2-acetyl-3-methyl->","23787-80-6","C7H8N2O",None,1079,None,1079),
("Pyrazine <2-acetyl-3-ethyl->","32974-92-8","C8H10N2O",None,1156,None,1156),
("Pyrazine <methylthio->","21948-70-9","C5H6N2S",None,1093,None,1093),
("Isopropyl-2-methoxypyrazine <3->","25773-40-4","C8H12N2O",None,1090,None,1090),
("Methoxy-3-(1-methylpropyl)pyrazine <2->","24168-70-5","C9H14N2O",None,1168,None,1168),
("Acetylpyrrole <2->","1072-83-9","C6H7NO",None,1054,None,1054),
("Acetylfuran <2->","1192-62-7","C6H6O2",None,909,None,909),
("Furan <2-acetyl-5-methyl->","1193-79-9","C7H8O2",None,1031,None,1031),
("Acetyl thiophene <2->","88-15-3","C6H6OS",None,1086,None,1086),
("Thiophene <2-butyl->","1455-20-5","C8H12S",None,1057,None,1057),
("Furfuryl methyl sulfide","1438-91-1","C6H8OS",None,998,None,998),
("Difurfuryl sulfide","13678-67-6","C10H10O2S",None,1459,None,1459),
("Disulfide <diphenyl->","882-33-7","C12H10S2",None,1825,None,1825),
("Disulfide <dipropyl->","629-19-6","C6H14S2",None,1102,None,1102),
("Benzeneacetonitrile","140-29-4","C8H7N",None,1134,None,1134),
("Benzene acetonitrile <3-methoxy->","19924-43-7","C9H9NO",None,1375,None,1375),
]

# Merge into main database
REF_DB.extend(EXTRA_DB)

# ============================================================
# SYNONYMS
# ============================================================
SYNONYMS = {
"α-Thujene":["alpha-Thujene","3-Thujene","Thujene","Origanene"],
"α-Pinene":["alpha-Pinene","2-Pinene","Pin-2(3)-ene","Acintene A"],
"Camphene":["2,2-Dimethyl-3-methylene-bicyclo[2.2.1]heptane","Comphene"],
"Sabinene":["4(10)-Thujene","Sabinen","Thuj-4(10)-ene"],
"β-Pinene":["beta-Pinene","2(10)-Pinene","Nopinene","Pseudopinene"],
"Myrcene":["β-Myrcene","7-Methyl-3-methylene-1,6-octadiene","Myrcen"],
"α-Phellandrene":["alpha-Phellandrene","p-Mentha-1,5-diene"],
"δ-3-Carene":["3-Carene","Delta-3-Carene","Car-3-ene"],
"α-Terpinene":["alpha-Terpinene","p-Mentha-1,3-diene"],
"p-Cymene":["para-Cymene","1-Isopropyl-4-methylbenzene","p-Cymol","Dolcymene","p-Isopropyltoluene"],
"Limonene":["D-Limonene","Dipentene","Cinene","p-Mentha-1,8-diene"],
"β-Phellandrene":["beta-Phellandrene","p-Mentha-1(7),2-diene"],
"1,8-Cineole":["Eucalyptol","Cajeputol","Cineole","Cineol"],
"Eucalyptus":["Eucalyptol","Cineole","1,8-Cineole","Cajeputol"],
"(Z)-β-Ocimene":["cis-β-Ocimene","cis-beta-Ocimene"],
"(E)-β-Ocimene":["trans-β-Ocimene","trans-beta-Ocimene"],
"γ-Terpinene":["gamma-Terpinene","p-Mentha-1,4-diene"],
"Terpinolene":["α-Terpinolene","p-Mentha-1,4(8)-diene","Isoterpinene"],
"Linalool":["Linalol","β-Linalool","Licareol","Coriandrol"],
"α-Thujone":["alpha-Thujone","cis-Thujone"],
"β-Thujone":["beta-Thujone","trans-Thujone"],
"Camphor":["2-Bornanone","Bornan-2-one","Gum camphor"],
"Citronellal":["3,7-Dimethyl-6-octenal","Rhodinal"],
"Isoborneol":["iso-Borneol"],
"Borneol":["endo-Borneol","Bornyl alcohol","Baros camphor"],
"Menthone":["p-Menthan-3-one"],
"Terpinen-4-ol":["4-Terpinenol","p-Menth-1-en-4-ol","Terpineol-4"],
"Menthol":["l-Menthol","p-Menthan-3-ol","Peppermint camphor"],
"α-Terpineol":["alpha-Terpineol","p-Menth-1-en-8-ol","Terpineol"],
"Myrtenal":["Pin-2-en-10-al","2-Pinen-10-al"],
"Verbenone":["2-Pinen-4-one"],
"Nerol":["cis-Geraniol"],
"Citronellol":["3,7-Dimethyl-6-octen-1-ol","Rhodinol"],
"Neral":["cis-Citral","Citral B"],
"Geraniol":["trans-Geraniol","Lemonol"],
"Geranial":["trans-Citral","Citral A"],
"Linalyl acetate":["Bergamiol","Bergamot oil","Linalool acetate"],
"Bergamiol":["Linalyl acetate","Bergamot oil"],
"Bornyl acetate":["Bornyl ethanoate","l-Bornyl acetate"],
"Thymol":["2-Isopropyl-5-methylphenol","Thyme camphor","5-Methyl-2-isopropylphenol"],
"Carvacrol":["2-p-Cymenol","Isothymol","2-Methyl-5-isopropylphenol"],
"α-Terpinyl acetate":["alpha-Terpinyl acetate","p-Menth-1-en-8-ol acetate"],
"Neryl acetate":["cis-Geranyl acetate","Nerol acetate"],
"Geranyl acetate":["trans-Geranyl acetate","Geraniol acetate"],
"α-Cubebene":["Cubebene"],
"α-Ylangene":["alpha-Ylangene"],
"α-Copaene":["Copaene","Aglaiene"],
"β-Bourbonene":["beta-Bourbonene"],
"β-Cubebene":["beta-Cubebene"],
"β-Elemene":["beta-Elemene","β-Elemen"],
"β-Elemen":["β-Elemene","beta-Elemene"],
"β-Caryophyllene":["BCP","(-)-trans-β-Caryophyllene","beta-Caryophyllene"],
"β-Copaene":["beta-Copaene"],
"α-Bergamotene":["trans-α-Bergamotene"],
"α-trans-Bergamotene":["α-Bergamotene","trans-α-Bergamotene"],
"Aromadendrene":["Aromadendren"],
"α-Gurjunene":["Gurjunene"],
"α-Humulene":["α-Caryophyllene","Humulene"],
"(E)-β-Farnesene":["trans-β-Farnesene"],
"allo-Aromadendrene":["allo-Aromadendren"],
"γ-Muurolene":["gamma-Muurolene"],
"Germacrene D":["Germacradiene D"],
"β-Selinene":["beta-Selinene","β-Eudesmene"],
"δ-Selinene":["delta-Selinene"],
"α-Muurolene":["alpha-Muurolene"],
"α-Selinene":["alpha-Selinene"],
"Bicyclogermacrene":["Bicyclogermacren"],
"β-Bisabolene":["beta-Bisabolene"],
"γ-Cadinene":["gamma-Cadinene"],
"δ-Cadinene":["delta-Cadinene","Cadina-1(10),4-diene"],
"α-Calacorene":["alpha-Calacorene"],
"α-Bisabolene":["alpha-Bisabolene"],
"β-Sesquiphellandrene":["beta-Sesquiphellandrene"],
"α-Zingiberene":["Zingiberene"],
"Valencene":["Valencen","Eremophila-1(10),11-diene"],
"(E,E)-α-Farnesene":["trans,trans-α-Farnesene"],
"Cuparene":["Cuparen"],
"α-Bulnesene":["alpha-Bulnesene"],
"α-Longipinene":["alpha-Longipinene"],
"δ-Elemene":["delta-Elemene"],
"α-Santalene":["alpha-Santalene"],
"α-Patchoulene":["alpha-Patchoulene"],
"Nerolidol (Z)":["cis-Nerolidol","Peruviol"],
"Nerolidol (E)":["trans-Nerolidol"],
"Spathulenol":["Spathulenol","Espatulenol"],
"Caryophyllene oxide":["Caryophyllene epoxide","β-Caryophyllene oxide"],
"Globulol":["Globulol"],
"Ledol":["Ledol"],
"Viridiflorol":["Viridiflorol"],
"Guaiol":["Champacol","Guaiol","Champaca camphor"],
"Cedrol":["Cedar camphor","8-β-Cedran-8-ol"],
"Cubenol":["Cubenol"],
"epi-α-Cadinol":["epi-alpha-Cadinol","τ-Cadinol"],
"α-Cadinol":["alpha-Cadinol"],
"α-Bisabolol":["Levomenol","Bisabolol","Dragosantol"],
"β-Bisabolol":["beta-Bisabolol"],
"(2E,6E)-Farnesol":["trans,trans-Farnesol"],
"(2Z,6E)-Farnesol":["cis,trans-Farnesol"],
"(2E,6Z)-Farnesol":["trans,cis-Farnesol"],
"(2Z,6Z)-Farnesol":["cis,cis-Farnesol"],
"Nootkatone":["Nootkatone","1(10),11-Eremophiladien-2-one"],
"Sclareol":["Sclareol"],
"Bulnesol":["Bulnesol","Guai-1(10)-en-11-ol"],
"α-Acorenol":["alpha-Acorenol"],
"Acorenone B":["Acorenone-B"],
"β-Eudesmol":["beta-Eudesmol","β-Selinene"],
"α-Eudesmol":["alpha-Eudesmol","α-Selinenol"],
"γ-Eudesmol":["gamma-Eudesmol"],
"10-epi-γ-Eudesmol":["10-epi-gamma-Eudesmol"],
"Juniperol":["Longiborneol","Macrocarpol"],
"Cedryl acetate":["Cedrol acetate","8-β-Cedran-8-ol acetate"],
"Patchouli alcohol":["Patchoulol"],
"Khusimol":["Khusimol","Zizanol","Tricyclovetivenol"],
"α-Vetivone":["alpha-Vetivone"],
"β-Vetivone":["beta-Vetivone"],
"Vetiselinenol":["Vetiselinenol"],
"Hinesol":["Hinesol"],
"Benzaldehyde":["Benzoic aldehyde","Phenylmethanal"],
"Methyl chavicol":["Estragole","p-Allylanisole","Isoanethole","1-Methoxy-4-(2-propenyl)benzene"],
"(E)-Anethole":["trans-Anethole","Anethol","Anise camphor","p-Propenylanisole"],
"Eugenol":["4-Allylguaiacol","Eugenic acid","4-Allyl-2-methoxyphenol"],
"Methyl eugenol":["Methyleugenol","Eugenol methyl ether"],
"(E)-Cinnamaldehyde":["trans-Cinnamaldehyde","Cinnamic aldehyde","3-Phenyl-2-propenal"],
"Benzyl acetate":["Benzyl ethanoate","α-Acetoxytoluene"],
"Benzyl alcohol":["Phenylcarbinol","Benzenemethanol","α-Hydroxytoluene"],
"2-Phenylethyl alcohol":["Phenethyl alcohol","β-Phenylethanol","Benzyl carbinol"],
"Methyl salicylate":["Oil of wintergreen","Wintergreen oil","2-Carbomethoxyphenol"],
"Vanillin":["Vanillic aldehyde","4-Hydroxy-3-methoxybenzaldehyde"],
"Thymol methyl ether":["Methyl thymol ether","2-Methoxy-4-methyl-1-(1-methylethyl)benzene"],
"Carvacrol methyl ether":["Methyl carvacrol ether","2-Methoxy-1-methyl-4-(1-methylethyl)benzene"],
"Hexanal":["Caproaldehyde","n-Hexanal"],
"(E)-2-Hexenal":["trans-2-Hexenal","Leaf aldehyde"],
"(Z)-3-Hexenol":["cis-3-Hexen-1-ol","Leaf alcohol"],
"1-Hexanol":["Hexyl alcohol","n-Hexanol","Caproyl alcohol"],
"Heptanal":["Heptaldehyde","n-Heptanal","Enanthaldehyde"],
"Octanal":["Caprylaldehyde","n-Octanal"],
"Nonanal":["n-Nonanal","Pelargonaldehyde"],
"Decanal":["n-Decanal","Capraldehyde"],
"Benzeneacetaldehyde":["Phenylacetaldehyde","Phenylethanal"],
"Furfural":["2-Furaldehyde","Furfuraldehyde","2-Formylfuran"],
"5-Methylfurfural":["5-Methyl-2-furaldehyde"],
"(E)-β-Damascenone":["trans-β-Damascenone","Damascenone"],
"Jasmone (Z)":["cis-Jasmone","Jasmone"],
"Methyl jasmonate":["Jasmonic acid methyl ester"],
"Dihydrojasmone":["2,3-Dihydrojasmone"],
"α-Ionone (E)":["trans-α-Ionone","α-Cyclocitrylideneacetone"],
"β-Ionone (E)":["trans-β-Ionone"],
"Geranylacetone":["Geranyl acetone","trans-Geranyl acetone"],
"Nootkatol":["Nootkatol","Nootkanol"],
"Cadalene":["Cadalene","Cadalin"],
"Chamazulene":["Chamazulene","Dimethulene"],
"Abietadiene":["Abieta-7,13-diene"],
"Manool":["Manool","Labda-8(20),14-dien-13-ol"],
"Manoyl oxide":["8α,13-Epoxylabd-14-ene"],
"Sclareolide":["Norambreinolide"],
"Phytol":["trans-Phytol","Phytol(E)-"],
"Hexadecanoic acid":["Palmitic acid","Cetylic acid"],
"Octadecanoic acid":["Stearic acid"],
"Linoleic acid":["Telfairic acid"],
"Oleic acid":["Oleinic acid"],
"(E)-β-Santalene":["trans-β-Santalene"],
"Santalol (Z, α)":["cis-α-Santalol"],
"Santalol (E, α)":["trans-α-Santalol"],
"β-Patchoulene":["beta-Patchoulene"],
"α-Springene":["alpha-Springene"],
"α-Fenchene":["alpha-Fenchene"],
"Verbenene":["2(10),3-Pinadiene"],
"Thuja-2,4(10)-diene":["4-Methylene-1-(1-methylethyl)bicyclo[3.1.0]hex-2-ene"],
"Isolimonene":["trans-Isolimonene"],
"Sylvestrene":["m-Mentha-1(6),8-diene"],
"Mentha-1(7),8-diene <p->":["Pseudolimonene"],
"Mentha-3,8-diene <p->":["p-Mentha-3,8-diene"],
"Mentha-2,4(8)-diene <p->":["Isoterpinolene","p-Mentha-2,4(8)-diene"],
"Pinane <trans->":["trans-Pinane"],
"Pinane <cis->":["cis-Pinane"],
"Cymene <o->":["o-Cymene","1-Methyl-2-(1-methylethyl)benzene"],
"Cymenene <p->":["Dehydro-p-cymene","4-Isopropenyltoluene"],
"Ocimene <allo->":["Alloocimene","(4E,6Z)-Alloocimene"],
"Ocimene <neo-allo->":["neo-Alloocimene","(4E,6E)-Alloocimene"],
"Artemisia triene":["2,5,5-Trimethyl-1,3,6-heptatriene"],
"Santolina triene":["3-Ethenyl-2,5-dimethyl-1,4-hexadiene"],
"Citronellene <β->":["Dihydromyrcene"],
"Salvene <E->":["trans-Salvene"],
"Salvene <Z->":["cis-Salvene"],
"Tricyclene":["Cyclene","1,7,7-Trimethyltricyclo[2.2.1.0(2,6)]heptane"],
"Santene":["2,3-Dimethylbicyclo[2.2.1]hept-2-ene"],
"Norbornene":["Norcamphene","Norfenchene"],
"1,4-Cineole":["p-Menthane,1,4-epoxy-","1,4-Epoxy-p-menthane"],
"Cineole <dehydro-1,8>":["Dehydro-1,8-cineole"],
"Linalool <dihydro->":["Dihydrolinalool","3,7-Dimethyl-6-octen-3-ol"],
"Linalool <tetrahydro->":["Tetrahydrolinalool","3,7-Dimethyloctan-3-ol"],
"Fenchol <endo->":["α-Fenchol"],
"Fenchol <exo->":["β-Fenchol"],
"Pinocarveol <cis->":["cis-Pinocarveol","2(10)-Pinen-3-ol,cis-"],
"Pinocarveol <trans->":["trans-Pinocarveol","2(10)-Pinen-3-ol"],
"Verbenol <cis->":["cis-Verbenol","2-Pinen-4-ol,cis-"],
"Verbenol <trans->":["trans-Verbenol","2-Pinen-4-ol,trans-"],
"Myrtenol":["2-Pinen-10-ol","Pin-2-en-10-ol"],
"Lavandulol":["2-Isopropenyl-5-methyl-4-hexen-1-ol"],
"Terpineol <β->":["β-Terpineol"],
"Terpineol <γ->":["γ-Terpineol"],
"Terpineol <δ->":["δ-Terpineol","p-Menth-1(7)-en-8-ol"],
"Terpineol <1->":["1-Terpineol","p-Menth-3-en-1-ol"],
"Menth-2-en-1-ol <cis-p->":["cis-p-Menth-2-en-1-ol"],
"Menth-2-en-1-ol <trans-p->":["trans-p-Menth-2-en-1-ol"],
"Menth-3-en-8-ol <p->":["p-Menth-3-en-8-ol"],
"Menth-1-en-9-ol <p->":["p-Menth-1-en-9-ol"],
"Carveol <cis->":["cis-Carveol","p-Mentha-6,8-dien-2-ol,cis-"],
"Carveol <trans->":["trans-Carveol","p-Mentha-6,8-dien-2-ol,trans-"],
"Dihydro carveol":["Dihydrocarveol","p-Menth-8-en-2-ol"],
"Dihydro carveol <iso->":["iso-Dihydrocarveol"],
"Dihydro carveol <neo->":["neo-Dihydrocarveol"],
"Dihydro carveol <neoiso->":["neoiso-Dihydrocarveol"],
"Pulegol <cis->":["cis-Pulegol"],
"Pulegol <trans->":["trans-Pulegol"],
"Isopulegol":["p-Menth-8-en-3-ol"],
"Isopulegol <iso->":["iso-Isopulegol"],
"Isopulegol <neo->":["neo-Isopulegol"],
"Isopulegol <neoiso->":["neoiso-Isopulegol"],
"Piperitol <cis->":["cis-Piperitol","p-Menth-1-en-3-ol,cis-"],
"Piperitol <trans->":["trans-Piperitol","p-Menth-1-en-3-ol,trans-"],
"Perilla alcohol":["Perillyl alcohol","p-Mentha-1,8-dien-7-ol"],
"Thujanol <3->":["3-Thujanol"],
"Thujanol <iso-3->":["iso-3-Thujanol","Isothujol"],
"Thujanol <neo-3->":["neo-3-Thujanol","Neothujol"],
"Thujanol <neoiso-3->":["neoiso-3-Thujanol","Neoisothujol"],
"Verbanol":["4-Pinanol"],
"Verbanol <iso->":["iso-Verbanol"],
"Verbanol <neo->":["neo-Verbanol"],
"Verbanol <neoiso->":["neoiso-Verbanol"],
"Pinocampheol":["3-Pinanol"],
"Myrtanol <cis->":["cis-Myrtanol"],
"Myrtanol <trans->":["trans-Myrtanol"],
"Nopol":["6,6-Dimethylbicyclo[3.1.1]hept-2-ene-2-ethanol"],
"Nerol oxide":["3,6-Dihydro-4-methyl-2-(2-methyl-1-propenyl)-2H-pyran"],
"Rose oxide <cis->":["cis-Rose oxide","(-)-Rose oxide"],
"Rose oxide <trans->":["trans-Rose oxide","(+)-Rose oxide"],
"Linalool oxide <cis-> (furanoid)":["cis-Linalool oxide (furanoid)","Linalool oxide B"],
"Linalool oxide <trans-> (furanoid)":["trans-Linalool oxide (furanoid)","Linalool oxide A"],
"Linalool oxide <cis-> (pyranoid)":["cis-Linalool oxide (pyranoid)","Linalool oxide D"],
"Linalool oxide <trans-> (pyranoid)":["trans-Linalool oxide (pyranoid)","Linalool oxide C"],
"Fenchone":["1,3,3-Trimethylbicyclo[2.2.1]heptan-2-one","1,3,3-Trimethylnorcamphor"],
"Menthone <iso->":["Isomenthone","cis-p-Menthan-3-one"],
"Pulegone":["p-Menth-4(8)-en-3-one","5-Methyl-2-(1-methylethylidene)cyclohexanone"],
"Piperitone":["p-Menth-1-en-3-one","3-Carvomenthenone"],
"Piperitenone":["p-Menth-1,4(8)-dien-3-one"],
"Carvone":["p-Mentha-6,8-dien-2-one","2-Methyl-5-(1-methylethenyl)-2-cyclohexenone"],
"Dihydro carvone <cis->":["cis-Dihydrocarvone","p-Menth-8-en-2-one,cis-"],
"Dihydro carvone <trans->":["trans-Dihydrocarvone","p-Menth-8-en-2-one,trans-"],
"Carvotanacetone":["p-Mentha-6-en-2-one","2-Methyl-5-(1-methylethyl)-2-cyclohexenone"],
"Carvone oxide <cis->":["cis-Carvone oxide"],
"Carvone oxide <trans->":["trans-Carvone oxide"],
"Carvone hydrate":["8-Hydroxy-p-menth-6-en-2-one"],
"Pinocarvone":["2(10)-Pinen-3-one","3-Nopinenone"],
"Pinocamphone <cis->":["cis-3-Pinanone","isopinocamphone"],
"Pinocamphone <trans->":["trans-3-Pinanone"],
"Nopinone":["6,6-Dimethylbicyclo[3.1.1]heptan-2-one"],
"Camphenilone":["3,3-Dimethylbicyclo[2.2.1]heptan-2-one"],
"Chrysanthenone":["2,7,7-Trimethylbicyclo[3.1.1]hept-2-en-6-one"],
"Umbellulone":["3-Thujen-2-one","4-Methyl-1-(1-methylethyl)bicyclo[3.1.0]hex-3-en-2-one"],
"Cryptone":["4-Isopropyl-2-cyclohexen-1-one"],
"Menthofuran":["4,5,6,7-Tetrahydro-3,6-dimethylbenzofuran","p-Mentha-3,8-diene,3,9-epoxy-"],
"Eucarvone":["2,6,6-Trimethyl-2,4-cycloheptadien-1-one"],
"Karahanaenone":["2,2,5-Trimethyl-4-cyclohepten-1-one"],
"Sabina ketone":["5-Isopropylbicyclo[3.1.0]hexan-2-one"],
"Isophorone":["Isoacetophorone","3,5,5-Trimethyl-2-cyclohexen-1-one"],
"Dihydroisojasmone":["2-Hexylcyclopentanone"],
"Jasmone <(E)->":["trans-Jasmone"],
"Jasmone <dihydro->":["2,3-Dihydrojasmone"],
"Methyl dihydro jasmonate <trans->":["Hedione","Methyl trans-dihydrojasmonate"],
"Linalool acetate <dihydro->":["Dihydrolinalyl acetate"],
"Linalool acetate <tetrahydro->":["Tetrahydrolinalyl acetate"],
"Linalool formate":["Linalyl formate"],
"Linalool propanoate":["Linalyl propionate"],
"Linalool butanoate":["Linalyl butyrate"],
"Linalool isobutanoate":["Linalyl isobutyrate"],
"Linalool isovalerate":["Linalyl isovalerate"],
"Isobornyl acetate":["Isoborneol acetate","exo-Bornyl acetate"],
"Isobornyl formate":["Isoborneol formate"],
"Isobornyl propanoate":["Isoborneol propionate"],
"Isobornyl n-butanoate":["Isoborneol butyrate"],
"Isobornyl isobutanoate":["Isoborneol isobutyrate"],
"Isobornyl isovalerate":["Isoborneol isovalerate","Gynoval"],
"Bornyl angelate":["Bornyl angelate"],
"Fenchyl acetate <endo->":["α-Fenchyl acetate"],
"Fenchyl acetate <exo->":["β-Fenchyl acetate"],
"Terpinyl isobutanoate <α->":["α-Terpinyl isobutyrate"],
"Geranyl formate":["Geraniol formate"],
"Geranyl propanoate":["Geranyl propionate"],
"Geranyl butanoate":["Geranyl butyrate","Geraniol butanoate"],
"Geranyl isobutanoate":["Geranyl isobutyrate"],
"Geranyl isovalerate":["Geranyl 3-methylbutanoate"],
"Geranyl tiglate":["Tiglic acid geranyl ester"],
"Geranyl valerate":["Geranyl pentanoate","Geraniol pentanoate"],
"Geranyl 2-methyl butanoate":["Geranyl 2-methylbutyrate"],
"Geranyl benzoate":["Geraniol benzoate"],
"Neryl formate":["Nerol formate"],
"Neryl propanoate":["Neryl propionate"],
"Neryl isobutanoate":["Neryl isobutyrate"],
"Neryl isovalerate":["Neryl 3-methylbutanoate"],
"Nerolidyl acetate <(E)->":["trans-Nerolidyl acetate"],
"Nerolidyl acetate <(Z)->":["cis-Nerolidyl acetate"],
"Citronellyl acetate":["Citronellol acetate"],
"Citronellyl formate":["Citronellol formate"],
"Citronellyl propanoate":["Citronellyl propionate"],
"Citronellyl butanoate":["Citronellyl butyrate","Citronellol butanoate"],
"Citronellyl isobutanoate":["Citronellol isobutyrate"],
"Citronellyl pentanoate":["Citronellyl valerate"],
"Citronellyl tiglate":["Tiglic acid citronellyl ester"],
"Citronellyl oxy-acetaldehyde":["Citronellyloxyacetaldehyde"],
"Lavandulyl acetate":["Lavandulol acetate"],
"Lavandulyl isobutanoate":["Lavandulyl isobutyrate"],
"Lavandulyl isovalerate":["Lavandulol isovalerate"],
"Menthyl acetate":["l-Menthyl acetate"],
"Menthyl acetate <iso->":["iso-Menthyl acetate"],
"Menthyl acetate <neo->":["neo-Menthyl acetate"],
"Menthyl isovalerate":["Menthol isovalerate","Menthyl isopentanoate"],
"Menthyl lactate":["Menthyl lactate"],
"Carvyl acetate <cis->":["cis-Carvyl acetate","p-Mentha-6,8-dien-2-ol acetate,cis-"],
"Carvyl acetate <trans->":["trans-Carvyl acetate","p-Mentha-6,8-dien-2-ol acetate,trans-"],
"Carvyl propanoate <cis->":["cis-Carvyl propionate"],
"Carvyl propanoate <trans->":["trans-Carvyl propionate"],
"Dihydro carveol acetate":["Dihydrocarvyl acetate"],
"Dihydro carveol acetate <iso->":["iso-Dihydrocarvyl acetate"],
"Dihydro carveol acetate <neo->":["neo-Dihydrocarvyl acetate"],
"Dihydro carveol acetate <neoiso->":["neoiso-Dihydrocarvyl acetate"],
"Dihydro citronellol acetate":["Dihydrocitronellyl acetate","Tetrahydrogeranyl acetate"],
"Dihydro myrcenol acetate":["Dihydromyrcenyl acetate"],
"Myrtenyl acetate":["2-Pinen-10-ol acetate"],
"Myrtanol acetate <trans->":["trans-Myrtanyl acetate"],
"Pinocarvyl acetate <cis->":["cis-Pinocarvyl acetate"],
"Pinocarvyl acetate <trans->":["trans-Pinocarvyl acetate"],
"Verbenyl acetate <cis->":["cis-Verbenyl acetate"],
"Verbenyl acetate <trans->":["trans-Verbenyl acetate"],
"Sabinyl acetate <trans->":["trans-Sabinyl acetate"],
"Thujanol acetate <3->":["3-Thujanyl acetate"],
"Thujanol acetate <iso-3->":["iso-3-Thujanyl acetate"],
"Thujanol acetate <neo-3->":["neo-3-Thujanyl acetate"],
"Thujanol acetate <neoiso-3->":["neoiso-3-Thujanyl acetate"],
"Sabinene hydrate acetate <cis->":["cis-4-Thujanol acetate","cis-Sabinene hydrate acetate"],
"Sabinene hydrate acetate <trans->":["trans-4-Thujanol acetate","trans-Sabinene hydrate acetate"],
"Isopulegyl acetate":["Isopulegol acetate"],
"Piperitol acetate <cis->":["cis-Piperityl acetate"],
"Piperitol acetate <trans->":["trans-Piperityl acetate"],
"Carvomenthyl acetate <neoiso->":["neoiso-Carvomenthyl acetate"],
"Cymen-7-ol acetate <p->":["p-Cuminyl acetate"],
"Menth-1-en-9-ol acetate <p->":["p-Menth-1-en-9-ol acetate"],
"Terpinen-4-ol acetate":["4-Terpinenyl acetate"],
"Nopyl acetate":["Nopol acetate","Citroviol"],
"Methyl myrtenate":["Myrtenic acid methyl ester"],
"Methyl thujate":["Thujic acid methyl ester"],
"Methyl perillate":["Perillic acid methyl ester"],
"Methyl citronellate":["Citronellic acid methyl ester"],
"Methyl geranate":["Geranic acid methyl ester","Methyl geraniate"],
"Methyl nerolate":["Neric acid methyl ester"],
"Ethyl nerolate":["Ethyl (Z)-geranate"],
"Ethyl geranate":["Ethyl (E)-geranate"],
"Anethole <(Z)->":["cis-Anethole","cis-p-Methoxy-β-methylstyrene"],
"Eugenol acetate":["Acetyleugenol"],
"Eugenol <dihydro->":["4-Propylguaiacol","Cerulignol"],
"Isoeugenol <(E)->":["trans-Isoeugenol"],
"Isoeugenol <(Z)->":["cis-Isoeugenol"],
"Methyl isoeugenol <(E)->":["trans-Methylisoeugenol","4-trans-Propenyl veratrole"],
"Methyl isoeugenol <(Z)->":["cis-Methylisoeugenol"],
"Chavicol":["4-Allylphenol","p-Allylphenol"],
"Chavibetol acetate":["Chavicol acetate"],
"Cinnamaldehyde <(Z)->":["cis-Cinnamaldehyde"],
"Cinnamaldehyde <α-methyl->":["α-Methylcinnamaldehyde","2-Methyl-3-phenylacrolein"],
"Cinnamaldehyde <hydro->":["Hydrocinnamaldehyde","3-Phenylpropanal","Benzenepropanal"],
"Cinnamaldehyde <4-hydroxy-3-methoxy->":["Coniferaldehyde","Ferulaldehyde"],
"Cinnamaldehyde <(E)-p-methoxy->":["trans-p-Methoxycinnamaldehyde"],
"Methoxy cinnamaldehyde <(E)-o->":["trans-o-Methoxycinnamaldehyde"],
"Methoxy cinnamic acid <(4E)->":["trans-4-Methoxycinnamic acid"],
"Cinnamic acid <(E)->":["trans-Cinnamic acid","trans-β-Carboxystyrene"],
"Benzyl formate":["Benzyl methanoate"],
"Benzyl propanoate":["Benzyl propionate"],
"Benzyl butanoate":["Benzyl butyrate"],
"Benzyl isobutanoate":["Benzyl isobutyrate"],
"Benzyl tiglate":["Tiglic acid benzyl ester"],
"Benzyl benzoate":["Benylate","Ascabin","Ascabiol"],
"Benzyl salicylate":["Benzyl o-hydroxybenzoate"],
"Benzyl cinnamate":["Benzyl 3-phenylprop-2-enoate","Cinnamyl benzoate"],
"Benzyl acetylacetate":["Benzyl 3-oxobutanoate"],
"Phenyl ethyl acetate <1->":["α-Phenylethyl acetate","Styralyl acetate","Gardenol"],
"Phenyl ethyl formate <2->":["Phenethyl formate","Benzylcarbinyl formate"],
"Phenyl ethyl propanoate <2->":["Phenethyl propionate"],
"Phenyl ethyl butanoate <2->":["Phenethyl butyrate"],
"Phenyl ethyl isobutanoate":["Phenethyl isobutyrate","Styralyl isobutyrate"],
"Phenyl ethyl 2-methylbutanoate":["Phenethyl 2-methylbutyrate"],
"Phenyl ethyl 3-methyl butanoate":["Phenethyl isovalerate"],
"Phenyl ethyl hexanoate":["Phenethyl caproate"],
"Phenyl ethyl octanoate":["Phenethyl caprylate"],
"Phenyl ethyl tiglate <2->":["Phenethyl tiglate"],
"Phenyl ethyl phenyl acetate <2->":["Phenethyl phenylacetate"],
"Phenyl ethyl anthranilate <2->":["Phenethyl anthranilate"],
"Phenyl ethyl oxyacetaldehyde":["Phenethyloxyacetaldehyde"],
"Phenethyl 2-furoate":["2-Furoic acid phenethyl ester"],
"Phenethyl cinnamate":["Cinnamic acid phenethyl ester"],
"Ethyl salicylate":["Salicylic acid ethyl ester"],
"Butyl salicylate":["n-Butyl salicylate"],
"Hexyl salicylate":["n-Hexyl salicylate"],
"Isobutyl salicylate":["Isobutyl o-hydroxybenzoate"],
"Isopentyl salicylate":["Isoamyl salicylate","Salicylic acid isopentyl ester"],
"Pentyl salicylate":["Amyl salicylate"],
"Salicylaldehyde":["2-Hydroxybenzaldehyde","Salicylal"],
"Vanillin <ethyl->":["Ethylvanillin","3-Ethoxy-4-hydroxybenzaldehyde","Ethylprotal"],
"Vanillin <o->":["o-Vanillin","2-Hydroxy-3-methoxybenzaldehyde"],
"Vanillin acetate":["Acetovanillin","Acetylvanillin"],
"Vanillone, aceto-":["Acetoguaiacone","Apocynine"],
"Vanillyl alcohol":["4-Hydroxy-3-methoxybenzyl alcohol"],
"Methyl vanillin":["Veratraldehyde","3,4-Dimethoxybenzaldehyde"],
"Syringaldehyde":["4-Hydroxy-3,5-dimethoxybenzaldehyde","Cedar aldehyde"],
"Syringol":["2,6-Dimethoxyphenol","Pyrogallol 1,3-dimethyl ether"],
"Cresol <o->":["2-Methylphenol","o-Cresol","o-Tolulol"],
"Cresol <m->":["3-Methylphenol","m-Cresol","m-Tolulol"],
"Cresol <p->":["4-Methylphenol","p-Cresol","p-Tolulol","p-Oxytoluene"],
"Cresol methyl ether <o->":["o-Methylanisole","1-Methoxy-2-methylbenzene"],
"Cresol acetate <o->":["o-Tolyl acetate","2-Acetoxytoluene"],
"Cresol acetate <m->":["m-Tolyl acetate","Cresatin","3-Acetoxytoluene"],
"Cresol acetate <p->":["p-Tolyl acetate","Cresyl acetate"],
"Cresol <2-methoxy-p->":["Creosol","4-Methylguaiacol"],
"Cresol isobutyrate <p->":["p-Tolyl isobutyrate"],
"Guaiacol <o->":["o-Methoxyphenol","Anastil","Pyroguaiac acid"],
"Guaiacol <p-vinyl->":["p-Vinylguaiacol","2-Methoxy-4-vinylphenol"],
"Guaiacol acetate <o->":["o-Acetoxyanisole","Eucol","2-Methoxyphenyl acetate"],
"Methyoxythiophenol <2->":["Thioguaiacol","2-Mercaptoanisole"],
"Anisaldehyde <p->":["Anisic aldehyde","Crategine","Aubepine","p-Formylanisole"],
"Anisaldehyde <o->":["o-Methoxybenzaldehyde","Salicylaldehyde methyl ether"],
"Anisaldehyde, <meta->":["m-Anisaldehyde","3-Methoxybenzaldehyde"],
"Anisyl alcohol <p->":["p-Methoxybenzyl alcohol","Anise alcohol"],
"Anisyl alcohol <meta->":["m-Anisyl alcohol","3-Methoxybenzyl alcohol"],
"Anisyl acetate <p->":["p-Methoxybenzyl acetate"],
"Anisyl formate":["p-Methoxybenzyl formate"],
"Anisyl propanoate":["Anisyl propionate"],
"Anisyl methyl ketone":["4-Methoxyphenylacetone","Anisalacetone","Anisketone"],
"Anisole":["Methoxybenzene","Methyl phenyl ether"],
"Anisole <p-methyl->":["p-Methylanisole","p-Methoxytoluene","p-Cresol methyl ether"],
"Acetophenone":["Phenyl methyl ketone","Acetylbenzene","Hypnone","Phenylethanone"],
"Acetophenone <p-methyl->":["p-Methylacetophenone","4-Methylacetophenone","p-Acetyltoluene"],
"Acetophenone <3'-methoxy->":["m-Methoxyacetophenone","Acetanisole,meta-"],
"Acetophenone <4'-methoxy->":["4-Methoxyacetophenone","Acetanisole,p-","Linarodin"],
"Acetanisole <o->":["o-Methoxyacetophenone"],
"Ethyl acetophenone <p->":["p-Acetylethylbenzene","1-(4-Ethylphenyl)ethanone"],
"Hydroxy acetophenone <2'->":["2-Hydroxyacetophenone","o-Acetophenol"],
"Hydroxybenzaldehyde <4->":["p-Hydroxybenzaldehyde","p-Formylphenol"],
"Benzenemethanol <2-hydroxy->":["Salicyl alcohol","Saligenin","Diathesin"],
"Benzene methanol <α-methyl->":["α-Phenylethyl alcohol","Styralyl alcohol","1-Phenylethanol"],
"Phenyl propanal <2->":["2-Phenylpropanal","Cumene aldehyde","Hyacinthal"],
"Hydrocinnamyl alcohol":["3-Phenylpropanol","3-Benzenepropanol","Hydrocinnamic alcohol"],
"Hydrocinnamyl acetate":["3-Phenylpropyl acetate"],
"Cyclamen aldehyde":["Cyclamal","2-Methyl-3-(p-isopropylphenyl)propanal"],
"Lilial":["Lilyal","p-tert-Butyl-α-methylhydrocinnamaldehyde"],
"Methyl benzoate":["Niobe oil","Oil of Niobe","Clorius"],
"Ethyl benzoate":["Benzoic acid ethyl ester","Benzoyl ethyl ether"],
"Methyl cinnamate <(E)->":["trans-Methyl cinnamate"],
"Methyl cinnamate <(Z)->":["cis-Methyl cinnamate"],
"Ethyl cinnamate <(E)->":["trans-Ethyl cinnamate"],
"Ethyl cinnamate <(Z)->":["cis-Ethyl cinnamate"],
"Cinnamyl alcohol <(E)->":["trans-Cinnamyl alcohol","Stryryl carbinol"],
"Cinnamyl alcohol <(Z)->":["cis-Cinnamyl alcohol"],
"Cinnamyl acetate <(E)->":["trans-Cinnamyl acetate"],
"Cinnamyl acetate <(Z)->":["cis-Cinnamyl acetate"],
"Benzoin":["2-Hydroxy-1,2-diphenylethanone","Desyl alcohol"],
"Benzophenone":["Diphenyl ketone","Benzoylbenzene"],
"Benzofuran <2,3-dimethyl->":["2,3-Dimethylbenzofuran"],
"Benzene <pentyl->":["Amylbenzene","Phenylpentane","Pentylbenzene"],
"Benzene <1,3-dimethoxy->":["Resorcinol dimethyl ether","m-Methoxyanisole"],
"Benzaldehyde, dimethyl acetal":["Phenyl dimethoxymethane"],
"Dimethoxybenzene <1,4->":["Hydroquinone dimethyl ether","p-Methoxyanisole"],
"Dimethyl phenol <2,6->":["2,6-Xylenol"],
"Orcinol":["5-Methylresorcinol","3,5-Dihydroxytoluene"],
"Catechol <3-methyl->":["3-Methylcatechol","2,3-Dihydroxytoluene"],
"Phenol <2-allyl->":["o-Allylphenol"],
"Phenol <2-(1E)-propenyl->":["trans-2-Propenylphenol"],
"Phenol <2-(1Z)-propenyl->":["cis-2-Propenylphenol"],
"Phenol <2,6-dimethoxy->":["Syringol"],
"Indole":["1-Azaindene","1-Benzazole","2,3-Benzopyrrole","Ketole"],
"Skatole":["3-Methylindole"],
"Isoquinoline":["Benzopyridine","Leucoline","2-Azanaphthalene"],
"Nicotine":["3-(1-Methyl-2-pyrrolidinyl)pyridine"],
"Biphenyl":["Diphenyl","Bibenzene","Phenylbenzene"],
"Methyl biphenyl <4->":["4-Methylbiphenyl","p-Phenyltoluene"],
"Naphthalene":["Moth flakes","Tar camphor","Naphthalin"],
"Naphthalene <1-methoxy->":["1-Methoxynaphthalene"],
"Naphthalene <2-methoxy->":["2-Methoxynaphthalene","Nerolin","Yara yara"],
"Azulene":["Cyclopentacycloheptene"],
"Guaiazulene":["1,4-Dimethyl-7-isopropylazulene","Azulon"],
"α-Cadinene":["alpha-Cadinene"],
"Cedrene <α->":["alpha-Cedrene","Cedr-8-ene"],
"Cedrene <β->":["beta-Cedrene","Cedr-8(15)-ene"],
"Cuprenene <α->":["alpha-Cuprenene"],
"Cyclosativene":["Cyclosativene"],
"Daucene":["Daucene"],
"Germacrene A":["Germacrene A"],
"Germacrene B":["Germacrene B","Germacra-1(10),4,7(11)-triene"],
"Gurjunene <β->":["beta-Gurjunene","Calarene"],
"Gurjunene <γ->":["gamma-Gurjunene"],
"Himachalene <α->":["alpha-Himachalene"],
"Himachalene <β->":["beta-Himachalene"],
"Himachalene <γ->":["gamma-Himachalene"],
"Humulene <β->":["beta-Humulene"],
"Ishwarane":["Ishwarane"],
"Isocomene <α->":["alpha-Isocomene","Berkheyaradulene"],
"Isocomene <β->":["beta-Isocomene"],
"Isoledene":["Isoledene"],
"Italicene":["Italicene"],
"Khusimene":["Khusimene","Tricyclovetivene","Zizaene"],
"Ledene":["Ledene","Viridiflorene"],
"Longicyclene":["Longicyclene"],
"Longifolene":["Longifolene","Junipene","Kuromatsuene"],
"Longipinene <β->":["beta-Longipinene"],
"Modheph-2-ene":["Modhephene"],
"Nootkatene":["Nootkatene"],
"Occidentalol":["Occidentalol"],
"Panasinsene <β->":["beta-Panasinsene"],
"Prezizaene":["Prezizaene"],
"Pseudowiddrene":["Pseudowiddrene"],
"Rotundene":["Rotundene"],
"Sativene":["Sativene"],
"Sesquithujene":["Sesquithujene"],
"Seychellene":["Seychellene"],
"Silphiperfol-5-ene":["Silphiperfol-5-ene"],
"Silphiperfol-6-ene":["Silphiperfol-6-ene"],
"Silphinene":["Silphinene"],
"Thujopsene <cis->":["cis-Thujopsene","Widdrene","Sesquichamene"],
"Thujopsadiene <cis->":["cis-Thujopsadiene"],
"Vetispirene <α->":["alpha-Vetispirene"],
"Vetispirene <β->":["beta-Vetispirene"],
"Vetivenene <β->":["beta-Vetivenene"],
"Vetivenene <γ->":["gamma-Vetivenene"],
"Viridiflorene":["Viridiflorene","Ledene"],
"Zierone":["Zierone","Elleryone"],
"Zonarene":["Zonarene"],
"Cedrol <epi->":["epi-Cedrol"],
"Cubenol <1-epi->":["1-epi-Cubenol"],
"τ-Cadinol":["tau-Cadinol","epi-α-Cadinol"],
"τ-Muurolol":["tau-Muurolol"],
"α-Muurolol":["alpha-Muurolol","Torreyol"],
"epi-α-Bisabolol":["epi-alpha-Bisabolol"],
"epi-β-Bisabolol":["epi-beta-Bisabolol"],
"Farnesol <2,3-dihydro->":["2,3-Dihydrofarnesol","Terrestrol"],
"Nootkatol <epi->":["epi-Nootkatol","Nootkanol"],
"β-Acorenol":["beta-Acorenol"],
"Acorenone":["Acorenone"],
"Eudesmol <dihydro->":["Dihydroeudesmol","Eudesman-11-ol"],
"Eudesm-7(11)-en-4-ol":["Selin-7(11)-en-4-ol","Juniper camphor"],
"Longiborneol":["Juniperol"],
"Hinesol acetate":["Hinesol acetate"],
"Valerianol":["Valerianol","Khusinol"],
"Agarospirol":["Agarospirol"],
"Pogostol":["Pogostol","Guai-11-en-10-ol"],
"Norpatchoulenol":["Norpatchoulenol"],
"Santalol <(Z)-β->":["cis-β-Santalol","Santalol b"],
"Santalol <(E)-β->":["trans-β-Santalol"],
"Santalol acetate <(Z)-α->":["cis-α-Santalol acetate"],
"Santalol acetate <(Z)-β->":["cis-β-Santalol acetate"],
"Santalol acetate <(E)-β->":["trans-β-Santalol acetate"],
"Bergamotol <(Z)-α-trans->":["cis-α-trans-Bergamotol"],
"Bergamotol acetate <(Z)-α-trans->":["cis-α-trans-Bergamotol acetate"],
"Lanceol <(Z)->":["cis-Lanceol"],
"Lanceol acetate <(Z)->":["cis-Lanceol acetate"],
"Nuciferol <(Z)->":["cis-Nuciferol"],
"Nuciferol <(E)->":["trans-Nuciferol"],
"Nuciferal <(Z)->":["cis-Nuciferal"],
"Nuciferal <(E)->":["trans-Nuciferal"],
"Nootkatin":["Nootkatin"],
"Nootkatinol":["Hydronootkatinol"],
"Elemicin":["1,2,3-Trimethoxy-5-(2-propenyl)benzene"],
"Isoelemicin <(E)->":["trans-Isoelemicin"],
"Isoelemicin <(Z)->":["cis-Isoelemicin"],
"Myristicin":["4-Methoxy-6-(2-propenyl)-1,3-benzodioxole"],
"Apiole":["Parsley apiole","Paioline","Parsley camphor"],
"Dill apiole":["4,5-Dimethoxy-6-(2-propenyl)-1,3-benzodioxole"],
"Safrole":["Shikimol","Rhyuno oil","4-Allyl-1,2-methylenedioxybenzene"],
"Isosafrole <(E)->":["trans-Isosafrole"],
"Isosafrole <(Z)->":["cis-Isosafrole"],
"Asarone <(E)->":["trans-Asarone","alpha-Asarone"],
"Asarone <(Z)->":["cis-Asarone","beta-Asarone"],
"Asarone <γ->":["gamma-Asarone","Sekishon","Euasarone"],
"Croweacin":["Croweacin"],
"Asaricin":["Sarisan"],
"Manool <13-epi->":["13-epi-Manool"],
"Manool oxide <13-epi->":["13-epi-Manoyl oxide"],
"Isophytol":["iso-Phytol"],
"Geranyl linalool <(E,E)->":["trans,trans-Geranyl linalool"],
"Pimaradiene":["Pimara-8(14),15-diene","Pimara-8,14-diene"],
"Sandaracopimara-8(14),15-diene":["Sandaracopimaradiene"],
"Sandaracopimarinol":["Isopimarinol","Sandaracopimaradienol"],
"Sandaracopimarinal":["Isodextropimaraldehyde"],
"Isopimarol":["Isopimarinol","Isopimara-7,15-dien-18-ol"],
"Methyl isopimarate":["Podocarp-8(14)-en-oic acid,13β-methyl-13-vinyl-,methyl ester"],
"Methyl pimarate":["Podocarp-8(14)-en-15-oic acid,13α-methyl-13-vinyl-,methyl ester"],
"Methyl sandaracopimarate":["Podocarp-8(14)-en-oic acid,13β-methyl-13-vinyl-,methyl ester"],
"Methyl dehydroabietate":["Podocarpa-8,11,13-trien-15-oic acid,13-isopropyl-,methyl ester"],
"Methyl abietate":["Podocarp-7,13-dien-15-oic acid,13-isopropyl-,methyl ester"],
"Methyl neoabietate":["Podocarp-8(14)-en-15-oic acid,13-isopropylidene-,methyl ester"],
"Methyl levopimarate":["Podocarpa-8(14),12-dien-15-oic acid,13-isopropyl-,methyl ester"],
"Abietal":["Abietinal","7,13-Abietadien-18-al"],
"Abietal <4-epi->":["4-epi-Abietinal"],
"Abietal <dehydro->":["Dehydroabietinal","Podocarpa-8,11,13-trien-15-al"],
"Abietatriene":["Dehydroabietane","Abieta-8,11,13-triene"],
"Abietadien-18-ol":["Podocarpa-8,13-diene,13-isopropyl-"],
"Abietol":["Abietinol","Podocarpa-7,13-dien-15-ol"],
"Abietol <4-epi->":["4-epi-Abietinol"],
"Abietol <neo->":["neo-Abietinol"],
"Abietol, dehydro":["Dehydroabietyl alcohol"],
"Abienol":["Labda-12,14-dien-8-ol"],
"Ferruginol <trans->":["trans-Ferruginol","Podocarpa-8,11,13-trien-12-ol,13-isopropyl-"],
"Ferruginol <6,7-dehydro->":["9-Dehydroferruginol"],
"Ferruginol <6-keto->":["6-Oxoferruginol"],
"Ferruginol acetate <trans->":["trans-Ferruginol acetate"],
"Totarol <trans->":["trans-Totarol","Podocarpa-8,11,13-trien-13-ol,14-isopropyl-"],
"Totarol acetate <trans->":["trans-Totarol acetate"],
"Totarolone":["Shonanol","3-Oxototarol"],
"Hinokiol":["Podocarpa-8,11,13-trien-3β,12-diol,13-isopropyl-"],
"Hinokione":["Podocarpa-8,11,13-trien-3-one,12-hydroxy-13-isopropyl-"],
"Hinokienone":["Podocarpa-1,8,11,13-tetraen-3-one,12-hydroxy-13-isopropyl-"],
"Sugiol":["Podocarpa-8,11,13-trien-7-one,12-hydroxy-13-isopropyl-"],
"Sempervirol":["Podocarpa-8,11,13-tiren-13-ol,12-isopropyl-"],
"Sclarene":["Labda-8(20),13(16),14-triene"],
"Rimuene":["Rosa-5,15-diene,(13S)-"],
"Beyerene":["Stachene","Hibaene"],
"Isohibaene":["13-Methyl-17-norkaur-15-ene"],
"Kaur-15-ene":["Isokaurene","Kryptomeren"],
"Kaurene":["16-Kaurene"],
"Isophyllocladene":["Kaur-15-ene,(5α,9α,10β)-"],
"Phyllocladene":["Kaur-16-ene,(8β,13β)-"],
"Cembrene":["Thunbergene"],
"Cembrene A <(3E)->":["neo-Cembrene"],
"Dolabradiene":["Dolabradiene"],
"Cubitene":["Cubitene"],
"Laurenene":["Laurenene"],
"Rosa-5,15-diene <ent->":["Rosadiene"],
"Incensole":["Incensole"],
"Incensole acetate":["Incensole acetate"],
"Incensole oxide":["Incensole oxide"],
"Larixol":["Labda-8(20),14-diene-6α,13-diol"],
"Torulosol":["Labda-8(20),14-diene-13,19-diol"],
"Methyl eperuate":["Eperuic acid,methyl ester"],
"Methyl communate <(Z)->":["Labda-8(20),12,14-trien-19-oic acid,methyl ester,(Z)-"],
"Methyl communate <(E)->":["Labda-8(20),12,14-trien-19-oic acid,methyl ester,(E)-"],
"Methyl labdanolate":["Labdanolic acid,methyl ester","Methyl 8-hydroxylabdan-15-oate"],
"Communic acid":["Labda-8(20),12,14-trien-19-oic acid"],
"Methyl daniellate":["Danedion","Danifos"],
"Thujaplicin <α->":["3-Isopropyltropolone","α-Thujaplicin"],
"Thujaplicin <β->":["β-Thujaplicin","Hinokitiol"],
"Thujaplicin <γ->":["5-Isopropyltropolone"],
"Methyl linoleate":["Linoleic acid methyl ester"],
"Methyl oleate":["Oleic acid methyl ester"],
"Methyl stearate":["Stearic acid methyl ester","Methyl octadecanoate"],
"Methyl palmitate":["Palmitic acid methyl ester","Methyl hexadecanoate"],
"Ethyl palmitate":["Palmitic acid ethyl ester"],
"Ethyl stearate":["Stearic acid ethyl ester"],
"Isopropyl palmitate":["Isopropyl hexadecanoate","Isopropyl myristate"],
"Ethyl myristate":["Myristic acid ethyl ester","Ethyl tetradecanoate"],
"Methyl myristate":["Myristic acid methyl ester","Methyl tetradecanoate"],
"Ethyl laurate":["Lauric acid ethyl ester","Ethyl dodecanoate"],
"Methyl laurate":["Lauric acid methyl ester","Methyl dodecanoate"],
"Ethyl decanoate":["Capric acid ethyl ester","Ethyl caprate"],
"Methyl decanoate":["Capric acid methyl ester","Methyl caprate"],
"Ethyl octanoate":["Caprylic acid ethyl ester","Ethyl caprylate"],
"Methyl octanoate":["Caprylic acid methyl ester","Methyl caprylate"],
"Ethyl hexanoate":["Ethyl caproate"],
"Methyl hexanoate":["Methyl caproate"],
"Butyl butanoate":["Butyl butyrate"],
"Butyl acetate":["Butyl ethanoate"],
"Butyl propanoate":["UN 1914","Propanoic acid,butyl ester"],
"Propyl butanoate":["Propyl butyrate"],
"Ethyl butanoate":["Ethyl butyrate"],
"Ethyl propanoate":["Ethyl propionate"],
"Methyl propanoate":["Methyl propionate"],
"Ethyl acetate":["Acetic ether","Acetidin","Ethyl ethanoate"],
"Hexyl acetate":["Acetic acid,hexyl ester"],
"Hexyl butanoate":["Hexyl butyrate"],
"Hexyl hexanoate":["Hexyl caproate"],
"Hexyl octanoate":["Hexyl caprylate"],
"Hexyl tiglate":["Crotonic acid,2-methyl-,hexyl ester (E)-"],
"Hexyl isobutanoate":["Hexyl isobutyrate"],
"Hexyl isovalerate":["Hexyl 3-methylbutanoate","Hexyl isopentanoate"],
"Hexyl propanoate":["Hexyl propionate"],
"Pentyl butanoate":["Amyl butyrate","Pentyl butyrate"],
"Pentyl propanoate":["Amyl propionate","Pentyl propionate"],
"Isopentyl acetate":["Banana oil","Isoamyl acetate","Pear oil"],
"Isopentyl isobutyrate":["Isoamyl isobutyrate"],
"Isopentyl isovalerate":["Isoamyl isovalerate"],
"Isopentyl butanoate":["Isoamyl n-butyrate"],
"Isoamyl propionate":["Isopentyl propanoate"],
"Isoamyl octanoate":["Isopentyl octanoate","Isoamyl caprylate"],
"Isoamyl benzoate":["Isopentyl benzoate"],
"Isoamyl 3-(2-furan)propionate":["Isoamyl furylpropionate"],
"Hexane <n->":["n-Hexane"],
"Heptane":["Skellysolve C","n-Heptane"],
"Octane <n->":["n-Octane"],
"Nonane <n->":["n-Nonane"],
"Decane <n->":["n-Decane"],
"Undecane <n->":["Hendecane"],
"Dodecane <n->":["n-Dodecane"],
"Tridecane <n->":["n-Tridecane"],
"Tetradecane <n->":["n-Tetradecane"],
"Pentadecane <n->":["n-Pentadecane"],
"Hexadecane <n->":["Cetane"],
"Heptadecane <n->":["n-Heptadecane"],
"Octadecane <n->":["n-Octadecane"],
"Nonadecane <n->":["n-Nonadecane"],
"Eicosane <n->":["n-Eicosane"],
"Heneicosane <n->":["n-Heneicosane"],
"Docosane <n->":["n-Docosane"],
"Tricosane <n->":["n-Tricosane"],
"Tetracosane <n->":["n-Tetracosane"],
"Pentacosane <n->":["n-Pentacosane"],
"Hexacosane":["n-Hexacosane"],
"Heptacosane":["n-Heptacosane"],
"Octacosane":["n-Octacosane"],
"Nonacosane":["n-Nonacosane"],
"Triacontane":["n-Triacontane"],
"Untriacontane":["n-Hentriacontane"],
"Dotriacontane":["n-Dotriacontane"],
"Tritriacontane":["n-Tritriacontane"],
"Tetratriacontane":["n-Tetratriacontane"],
"Thiazole":["1,3-Thiazole"],
"Thiazole <4-methyl->":["4-Methylthiazole"],
"Pyrazine <methyl->":["Methylpyrazine"],
"Pyrazine <2-ethyl->":["Ethylpyrazine"],
"Pyrazine <2,3-dimethyl->":["2,3-Dimethylpyrazine"],
"Pyrazine <tetramethyl->":["Ligustrazine","Tetramethylpyrazine"],
"Acetylfuran <2->":["2-Furyl methyl ketone","α-Acetylfuran"],
"Acetylpyrrole <2->":["2-Pyrrolylethanone"],
"Acetyl thiophene <2->":["Methyl 2-thienyl ketone"],
"Furfuryl methyl sulfide":["2-((Methylthio)methyl)furan"],
"Difurfuryl sulfide":["Furfuryl sulfide"],
"Benzeneacetonitrile":["Phenylacetonitrile","Benzyl cyanide","α-Tolunitrile"],
"Benzene acetonitrile <3-methoxy->":["3-Methoxyphenylacetonitrile","3-Methoxybenzyl cyanide"],
}

# Reverse synonym index
_SYN_REV = {}
for _c, _ss in SYNONYMS.items():
    for _s in _ss:
        _SYN_REV.setdefault(_s.lower(), []).append(_c)

def get_synonyms(n): return SYNONYMS.get(n, [])

def find_canonical(name):
    if not name: return None
    n = name.strip().lower()
    for r in REF_DB:
        if r[0].lower() == n: return r
    for r in REF_DB:
        for s in SYNONYMS.get(r[0], []):
            if s.lower() == n: return r
    return None

def search_ref(q):
    q = q.strip().lower()
    if not q: return list(REF_DB)
    out, seen = [], set()
    for r in REF_DB:
        if id(r) in seen: continue
        if q in r[0].lower() or q in r[1].lower():
            out.append(r); seen.add(id(r)); continue
        for s in SYNONYMS.get(r[0], []):
            if q in s.lower():
                out.append(r); seen.add(id(r)); break
    return out

REF_KEYS = ("DB-1", "DB-5", "PEG", "Adams")

def match_percent(kc, kr):
    if kc is None or kr is None or kr == 0: return None
    return max(0.0, 100.0 - abs(kc - kr) * 2.0)

def match_all(kc, row):
    return {k: (v, match_percent(kc, v))
            for k, v in zip(REF_KEYS, (row[3], row[4], row[5], row[6]))}

def best_match(kc, row):
    if kc is None: return None
    best = None
    for k, v in zip(REF_KEYS, (row[3], row[4], row[5], row[6])):
        m = match_percent(kc, v)
        if m is None: continue
        if best is None or m > best[2]: best = (k, v, m)
    return best

def find_best_candidates(kc, tol=60):
    if kc is None: return []
    s = []
    for r in REF_DB:
        b = best_match(kc, r)
        if b and abs(kc - b[1]) <= tol:
            s.append((r, b[0], b[1], b[2]))
    s.sort(key=lambda x: -x[3])
    return s

TXT = {
"ar": {"title":"محلل الزيوت العطرية — GC-MS","sub":"حاسبة كوفاتس • التعريف • التقدير الكمي • قواعد مرجعية",
 "lang":"اللغة","author":"تأليف","t_home":"  الرئيسية  ","t_kri":"  حاسبة KRI  ","t_ak":"  الألكانات  ",
 "t_id":"  التعريف  ","t_q":"  التقدير الكمي  ","t_ref":"  قواعد البيانات  ","t_rep":"  التقرير  ",
 "home_w":"مرحباً بك","home_i":"أداة متكاملة لتحليل الزيوت العطرية","steps":"خطوات الطريقة",
 "s1":"1. تحضير العينة","s2":"2. تشغيل معيار الألكانات","s3":"3. تشغيل العينة",
 "s4":"4. حساب KRI","s5":"5. التعريف","s6":"6. التقدير الكمي","cond":"ظروف التشغيل","regions":"مناطق KRI",
 "warn":"⚠ تحذير","warntxt":"لا تستخدم حرارة حاقن أعلى من 250°C","refs":"المراجع",
 "refstxt":"Adams (2017) + Babushok (2011)","param":"المعامل","value":"القيمة",
 "c1":"حرارة الحاقن","c1v":"250 °C","c2":"حجم الحقن","c2v":"1 µL","c3":"نسبة الانقسام","c3v":"1:100",
 "c4":"الغاز الحامل","c4v":"He","c5":"برنامج الفرن","c5v":"50→280 °C","c6":"تأخير المذيب","c6v":"4.5 min",
 "c7":"التأين","c7v":"EI+ 70 eV","c8":"حرارة المصدر","c8v":"250 °C","c9":"مدى المسح","c9v":"50-500",
 "c10":"نمط المسح","c10v":"Full","c11":"العمود","c11v":"DB-5",
 "ak_title":"معيار الألكانات","ak_sub":"أدخل RT للألكانات","ak_c":"الكربون","ak_rt":"RT (min)",
 "ak_add":"إضافة","ak_del":"حذف","ak_clear":"مسح","ak_load":"افتراضي","ak_cnt":"عدد:","ak_loaded":"تم: {n}",
 "ak_hint":"نقرة مزدوجة للتعديل","k_title":"حاسبة KRI","k_sub":"Van den Dool & Kratz","k_rt":"RT (min):",
 "k_calc":"احسب","k_result":"KRI","k_before":"السابق","k_after":"اللاحق","k_batch":"دفعة:",
 "k_batchbtn":"احسب","k_none":"خارج النطاق","k_nofill":"أدخل RT","i_title":"التعريف",
 "i_sub":"المطابقة % لكل مرجع","i_name":"المركب","i_rt":"RT","i_kril":"KRI مرجعي","i_match":"المطابقة",
 "i_add":"إضافة","i_del":"حذف","i_clear":"مسح","i_example":"مثال","i_from_db":"اقتراح",
 "ihn":"#","ihc":"المركب","ihrt":"RT","ihkc":"KRI محسوب","ihl":"KRI مرجع","ihm":"Match%","ihr":"المرجع","ihs":"الحالة",
 "i_ok":"معرَّف","i_tent":"مبدئي","i_unk":"غير معرَّف","i_sum":"الكل: {t} | معرَّف: {o} | مبدئي: {p} | غير: {u}",
 "i_match_all":"المطابقة % لكل مرجع:","q_title":"التقدير الكمي","q_sub":"% = المساحة/الإجمالي",
 "q_name":"المركب","q_area":"المساحة","q_kri":"KRI","q_add":"إضافة","q_del":"حذف","q_clear":"مسح",
 "q_example":"مثال","q_calc":"احسب","q_excl_s":"استبعاد مذيب","q_excl_h":"استبعاد >2500",
 "qhn":"#","qhc":"المركب","qha":"المساحة","qhp":"%","qhk":"KRI","q_total":"الكل: {t:,.0f} | عدد: {n}",
 "ref_title":"قواعد البيانات","ref_sub":"بحث بالاسم أو CAS","ref_search":"🔍 بحث:","ref_clear":"مسح",
 "ref_use":"استخدام","ref_cnt":"{n} من {t}","ref_note":"المطابقة لكل المراجع",
 "rhn":"المركب","rhcas":"CAS","rhf":"الصيغة","rhd1":"DB-1","rhd5":"DB-5","rhpeg":"PEG","rha":"Adams",
 "rhsyn":"أسماء بديلة","ref_match":"Match%","ref_match_note":"% = 100 − |ΔKRI| × 2",
 "ref_nort":"أدخل RT","ref_add":"➕ إضافة","ref_new_title":"إضافة مركب","ref_name":"الاسم","ref_cas":"CAS",
 "ref_formula":"الصيغة","ref_db1":"DB-1","ref_db5":"DB-5","ref_peg":"PEG","ref_adams":"Adams",
 "ref_syn":"أسماء بديلة","ref_saved":"تمت الإضافة","rep_title":"التقرير","rep_gen":"إنشاء","rep_save":"حفظ",
 "rep_copy":"نسخ","rep_sample":"العينة:","rep_analyst":"المحلل:","saved":"تم الحفظ","copied":"تم النسخ",
 "ok":"موافق","cancel":"إلغاء","warning":"تنبيه","error":"خطأ","status":"جاهز",
 "footer":"Adams (2017) • Babushok (2011) • NIST","db_info":"قاعدة: {n} | أسماء: {s}"},
"en": {"title":"Essential Oil Analyzer","sub":"Kovats • Identification • Quantification",
 "lang":"Language","author":"Author","t_home":"  Home  ","t_kri":"  KRI  ","t_ak":"  Alkanes  ",
 "t_id":"  Identification  ","t_q":"  Quantification  ","t_ref":"  Databases  ","t_rep":"  Report  ",
 "home_w":"Welcome","home_i":"GC-MS Essential Oil Analyzer","steps":"Workflow",
 "s1":"1. Sample prep","s2":"2. Alkane standard","s3":"3. Sample run","s4":"4. Compute KRI",
 "s5":"5. Identification","s6":"6. Quantification","cond":"GC-MS","regions":"KRI Regions",
 "warn":"⚠ WARNING","warntxt":"Never exceed 250°C injector","refs":"References",
 "refstxt":"Adams (2017) + Babushok (2011)","param":"Parameter","value":"Value",
 "c1":"Injector","c1v":"250 °C","c2":"Volume","c2v":"1 µL","c3":"Split","c3v":"1:100",
 "c4":"Carrier","c4v":"He","c5":"Oven","c5v":"50→280 °C","c6":"Delay","c6v":"4.5 min",
 "c7":"Ionisation","c7v":"EI+ 70 eV","c8":"Source","c8v":"250 °C","c9":"Scan","c9v":"50-500",
 "c10":"Mode","c10v":"Full","c11":"Column","c11v":"DB-5",
 "ak_title":"Alkane Standard","ak_sub":"Enter RT","ak_c":"Carbon","ak_rt":"RT (min)",
 "ak_add":"Add","ak_del":"Delete","ak_clear":"Clear","ak_load":"Defaults","ak_cnt":"Count:","ak_loaded":"Loaded: {n}",
 "ak_hint":"Double-click to edit","k_title":"KRI Calculator","k_sub":"Van den Dool & Kratz","k_rt":"RT (min):",
 "k_calc":"Calculate","k_result":"KRI","k_before":"Before","k_after":"After","k_batch":"Batch:",
 "k_batchbtn":"Compute","k_none":"Out of range","k_nofill":"Enter RT","i_title":"Identification",
 "i_sub":"Match % per reference","i_name":"Compound","i_rt":"RT","i_kril":"Ref. KRI","i_match":"Match",
 "i_add":"Add","i_del":"Delete","i_clear":"Clear","i_example":"Example","i_from_db":"Suggest",
 "ihn":"#","ihc":"Compound","ihrt":"RT","ihkc":"KRI calc","ihl":"Ref KRI","ihm":"Match%","ihr":"Ref","ihs":"Status",
 "i_ok":"Identified","i_tent":"Tentative","i_unk":"Unknown","i_sum":"All: {t} | ok: {o} | tent: {p} | unk: {u}",
 "i_match_all":"Match % per reference:","q_title":"Quantification","q_sub":"% = Area/Total",
 "q_name":"Compound","q_area":"Area","q_kri":"KRI","q_add":"Add","q_del":"Delete","q_clear":"Clear",
 "q_example":"Example","q_calc":"Compute","q_excl_s":"Exclude solvent","q_excl_h":"Exclude >2500",
 "qhn":"#","qhc":"Compound","qha":"Area","qhp":"%","qhk":"KRI","q_total":"Total: {t:,.0f} | N: {n}",
 "ref_title":"Reference Databases","ref_sub":"Search by name or CAS","ref_search":"🔍 Search:","ref_clear":"Clear",
 "ref_use":"Use","ref_cnt":"{n} of {t}","ref_note":"Match per every reference",
 "rhn":"Compound","rhcas":"CAS","rhf":"Formula","rhd1":"DB-1","rhd5":"DB-5","rhpeg":"PEG","rha":"Adams",
 "rhsyn":"Synonyms","ref_match":"Match%","ref_match_note":"% = 100 − |ΔKRI| × 2",
 "ref_nort":"Enter RT","ref_add":"➕ Add","ref_new_title":"Add compound","ref_name":"Name","ref_cas":"CAS",
 "ref_formula":"Formula","ref_db1":"DB-1","ref_db5":"DB-5","ref_peg":"PEG","ref_adams":"Adams",
 "ref_syn":"Synonyms","ref_saved":"Added","rep_title":"Report","rep_gen":"Generate","rep_save":"Save",
 "rep_copy":"Copy","rep_sample":"Sample:","rep_analyst":"Analyst:","saved":"Saved","copied":"Copied",
 "ok":"OK","cancel":"Cancel","warning":"Warning","error":"Error","status":"Ready",
 "footer":"Adams (2017) • Babushok (2011) • NIST","db_info":"DB: {n} | Synonyms: {s}"},
"de": {"title":"Ätherisches Öl","sub":"Kovats • Identifizierung • Quantifizierung",
 "lang":"Sprache","author":"Autor","t_home":"  Start  ","t_kri":"  KRI  ","t_ak":"  Alkane  ",
 "t_id":"  Ident.  ","t_q":"  Quant.  ","t_ref":"  Datenbanken  ","t_rep":"  Bericht  ",
 "home_w":"Willkommen","home_i":"GC-MS Analysator","steps":"Workflow",
 "s1":"1. Probe","s2":"2. Alkan","s3":"3. Lauf","s4":"4. KRI","s5":"5. Ident","s6":"6. Quant",
 "cond":"GC-MS","regions":"KRI","warn":"⚠ WARNUNG","warntxt":"Nicht über 250°C","refs":"Referenzen",
 "refstxt":"Adams (2017) + Babushok (2011)","param":"Parameter","value":"Wert",
 "c1":"Injektor","c1v":"250 °C","c2":"Volumen","c2v":"1 µL","c3":"Split","c3v":"1:100",
 "c4":"Träger","c4v":"He","c5":"Ofen","c5v":"50→280 °C","c6":"Verzögerung","c6v":"4,5 min",
 "c7":"Ion.","c7v":"EI+ 70 eV","c8":"Quelle","c8v":"250 °C","c9":"Scan","c9v":"50-500",
 "c10":"Modus","c10v":"Voll","c11":"Säule","c11v":"DB-5",
 "ak_title":"Alkan-Standard","ak_sub":"RT eingeben","ak_c":"Kohlenstoff","ak_rt":"RT (min)",
 "ak_add":"Hinzufügen","ak_del":"Löschen","ak_clear":"Alles löschen","ak_load":"Standard","ak_cnt":"Anzahl:","ak_loaded":"Geladen: {n}",
 "ak_hint":"Doppelklick","k_title":"KRI-Rechner","k_sub":"Van den Dool & Kratz","k_rt":"RT (min):",
 "k_calc":"Berechnen","k_result":"KRI","k_before":"Vorher","k_after":"Nachher","k_batch":"Stapel:",
 "k_batchbtn":"Berechnen","k_none":"Außerhalb","k_nofill":"RT eingeben","i_title":"Identifizierung",
 "i_sub":"Match % pro Referenz","i_name":"Verbindung","i_rt":"RT","i_kril":"Ref. KRI","i_match":"Match",
 "i_add":"Hinzufügen","i_del":"Löschen","i_clear":"Alles löschen","i_example":"Beispiel","i_from_db":"Vorschlag",
 "ihn":"#","ihc":"Verbindung","ihrt":"RT","ihkc":"KRI ber","ihl":"Ref KRI","ihm":"Match%","ihr":"Ref","ihs":"Status",
 "i_ok":"Ident.","i_tent":"Vorläufig","i_unk":"Unbekannt","i_sum":"Gesamt: {t} | id: {o} | prov: {p} | unb: {u}",
 "i_match_all":"Match % pro Referenz:","q_title":"Quantifizierung","q_sub":"% = Fläche/Gesamt",
 "q_name":"Verbindung","q_area":"Fläche","q_kri":"KRI","q_add":"Hinzufügen","q_del":"Löschen","q_clear":"Löschen",
 "q_example":"Beispiel","q_calc":"Berechnen","q_excl_s":"Lösungsmittel aus.","q_excl_h":">2500 aus.",
 "qhn":"#","qhc":"Verbindung","qha":"Fläche","qhp":"%","qhk":"KRI","q_total":"Gesamt: {t:,.0f} | N: {n}",
 "ref_title":"Referenz-DBs","ref_sub":"Nach Name oder CAS","ref_search":"🔍 Suche:","ref_clear":"Löschen",
 "ref_use":"Verwenden","ref_cnt":"{n} von {t}","ref_note":"Match pro Referenz",
 "rhn":"Verbindung","rhcas":"CAS","rhf":"Formel","rhd1":"DB-1","rhd5":"DB-5","rhpeg":"PEG","rha":"Adams",
 "rhsyn":"Synonyme","ref_match":"Match%","ref_match_note":"% = 100 − |ΔKRI| × 2",
 "ref_nort":"RT eingeben","ref_add":"➕ Hinzufügen","ref_new_title":"Verbindung hinzufügen","ref_name":"Name","ref_cas":"CAS",
 "ref_formula":"Formel","ref_db1":"DB-1","ref_db5":"DB-5","ref_peg":"PEG","ref_adams":"Adams",
 "ref_syn":"Synonyme","ref_saved":"Hinzugefügt","rep_title":"Bericht","rep_gen":"Erstellen","rep_save":"Speichern",
 "rep_copy":"Kopieren","rep_sample":"Probe:","rep_analyst":"Analytiker:","saved":"Gespeichert","copied":"Kopiert",
 "ok":"OK","cancel":"Abbrechen","warning":"Warnung","error":"Fehler","status":"Bereit",
 "footer":"Adams (2017) • Babushok (2011) • NIST","db_info":"DB: {n} | Synonyme: {s}"},
}

DEFAULT_ALKANES = [(8,4.66),(9,8.12),(10,12.25),(11,16.33),(12,20.15),(13,23.71),
(14,27.05),(15,30.19),(16,33.16),(17,35.97),(18,38.65),(19,41.19),(20,43.62),
(21,45.94),(22,48.16),(23,50.29),(24,52.34),(25,54.29),(26,56.18),(27,58.01),
(28,59.77),(29,60.78),(30,61.48)]

EXAMPLE_IDENT = [("1,8-Cineole",14.4240,1035.3),("Linalyl acetate",23.0246,1254.3),
("α-Terpinyl acetate",26.3730,1351.2),("β-Bourbonene",27.6417,1389.2),
("β-Elemene",27.7855,1393.4),("α-Gurjunene",28.7790,1424.7),
("α-Bergamotene",29.1310,1436.2),("Germacrene D",30.7517,1488.1),
("α-Selinene",30.9470,1494.2),("Bicyclogermacrene",31.2129,1502.9),
("β-Santalene",43.4685,1958.7),("Sclareol",49.8721,2292.6)]

EXAMPLE_QUANT = [("1,8-Cineole",15900,1035),("Linalyl acetate",1742400,1254),
("α-Terpinyl acetate",126000,1351),("β-Bourbonene",600,1389),("β-Elemene",2100,1393),
("α-Gurjunene",3400,1425),("α-Bergamotene",600,1436),("Germacrene D",6500,1488),
("α-Selinene",300,1494),("Bicyclogermacrene",1100,1503),("β-Santalene",3200,1959),
("Sclareol",8097800,2293)]

def kri_from_rt(rt, alkanes):
    pts = sorted(alkanes, key=lambda x: x[1])
    if len(pts) < 2: return None
    if rt <= pts[0][1] or rt >= pts[-1][1]: return None
    for i in range(len(pts)-1):
        c1, t1 = pts[i]; c2, t2 = pts[i+1]
        if t1 <= rt <= t2 and t2 > t1:
            return 100.0*c1 + 100.0*(c2-c1)*((rt-t1)/(t2-t1)), c1, c2
    return None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lang = "ar"; self.alkanes = list(DEFAULT_ALKANES)
        self.ident_rows = []; self.quant_rows = []
        self.sample_name = tk.StringVar(value="Salvia Dominica CO2 extract")
        self.analyst_name = tk.StringVar(value=AUTHOR_EN)
        self.title("GC-MS Essential Oil Analyzer")
        self.geometry("1340x900"); self.minsize(1120,740)
        self.configure(bg=C["bg"]); self._setup_style(); self._build()

    def t(self, k, **kw):
        s = TXT[self.lang].get(k, k)
        return s.format(**kw) if kw else s

    @property
    def rtl(self): return self.lang == "ar"
    def ff(self): return "Tahoma" if self.lang == "ar" else "Segoe UI"

    def _setup_style(self):
        st = ttk.Style(self)
        try: st.theme_use("clam")
        except: pass
        st.configure("TNotebook", background=C["bg"], borderwidth=0)
        st.configure("TNotebook.Tab", background=C["bg2"], foreground=C["muted"],
                     padding=(16,10), font=(self.ff(),10,"bold"), borderwidth=0)
        st.map("TNotebook.Tab", background=[("selected", C["card"])],
               foreground=[("selected", C["primary"])])
        st.configure("TFrame", background=C["card"])
        st.configure("TLabel", background=C["card"], foreground=C["text"], font=(self.ff(),10))
        st.configure("TButton", background=C["card2"], foreground=C["text"],
                     font=(self.ff(),10,"bold"), borderwidth=0, padding=(14,8))
        st.map("TButton", background=[("active", C["primary2"])])
        st.configure("Accent.TButton", background=C["primary"], foreground="#042f2e",
                     font=(self.ff(),10,"bold"), borderwidth=0, padding=(14,8))
        st.map("Accent.TButton", background=[("active", C["primary2"])])
        st.configure("Danger.TButton", background="#7f1d1d", foreground="#fecaca",
                     font=(self.ff(),10,"bold"), borderwidth=0, padding=(14,8))
        st.configure("TEntry", fieldbackground=C["bg2"], foreground=C["text"], padding=6)
        st.configure("Treeview", background=C["bg2"], fieldbackground=C["bg2"],
                     foreground=C["text"], rowheight=26, font=(self.ff(),10))
        st.configure("Treeview.Heading", background=C["card2"], foreground=C["primary"],
                     font=(self.ff(),10,"bold"), padding=6)
        st.configure("TCheckbutton", background=C["card"], foreground=C["text"])
        st.configure("Vertical.TScrollbar", background=C["card2"],
                     troughcolor=C["bg2"], borderwidth=0)

    def _build(self):
        for w in self.winfo_children(): w.destroy()
        self._setup_style()
        h = tk.Frame(self, bg=C["bg2"], height=92); h.pack(fill="x", side="top")
        h.pack_propagate(False)
        left = tk.Frame(h, bg=C["bg2"]); left.pack(side="left", padx=24, pady=10)
        tk.Label(left, text="⬢", bg=C["bg2"], fg=C["primary"],
                 font=("Segoe UI",26,"bold")).pack(side="left", padx=(0,12))
        tb = tk.Frame(left, bg=C["bg2"]); tb.pack(side="left")
        tk.Label(tb, text=self.t("title"), bg=C["bg2"], fg=C["text"],
                 font=(self.ff(),15,"bold")).pack(anchor="w")
        tk.Label(tb, text=self.t("sub"), bg=C["bg2"], fg=C["muted"],
                 font=(self.ff(),9)).pack(anchor="w")
        nm = AUTHOR_AR if self.lang=="ar" else AUTHOR_EN
        tk.Label(tb, text=f"✎ {nm}", bg=C["bg2"], fg=C["gold"],
                 font=(self.ff(),9,"italic")).pack(anchor="w")
        right = tk.Frame(h, bg=C["bg2"]); right.pack(side="right", padx=24)
        tk.Label(right, text="🌐 " + self.t("lang"), bg=C["bg2"], fg=C["muted"]).pack(side="left", padx=(0,8))
        self.lang_var = tk.StringVar(value={"ar":"العربية","en":"English","de":"Deutsch"}[self.lang])
        cb = ttk.Combobox(right, textvariable=self.lang_var, state="readonly",
                          values=["العربية","English","Deutsch"], width=11)
        cb.pack(side="left"); cb.bind("<<ComboboxSelected>>", self._on_lang)

        self.nb = ttk.Notebook(self)
        self.nb.pack(fill="both", expand=True, padx=14, pady=(12,6))
        for attr, key in [("tab_home","t_home"),("tab_kri","t_kri"),("tab_ak","t_ak"),
                          ("tab_id","t_id"),("tab_q","t_q"),("tab_ref","t_ref"),("tab_rep","t_rep")]:
            f = ttk.Frame(self.nb); setattr(self, attr, f)
            self.nb.add(f, text=self.t(key))
        self._build_home(); self._build_kri(); self._build_ak()
        self._build_id(); self._build_q(); self._build_ref(); self._build_rep()

        sb = tk.Frame(self, bg=C["bg2"], height=28); sb.pack(fill="x", side="bottom")
        sb.pack_propagate(False)
        tk.Label(sb, text="  ● " + self.t("status"), bg=C["bg2"], fg=C["ok"]).pack(side="left")
        tk.Label(sb, text=self.t("footer") + "  ", bg=C["bg2"], fg=C["muted"],
                 font=(self.ff(),8)).pack(side="right")

    def _on_lang(self, _=None):
        m = {"العربية":"ar","English":"en","Deutsch":"de"}
        n = m.get(self.lang_var.get(), "en")
        if n != self.lang:
            self.lang = n; self._build()

    def _scroll(self, parent):
        out = tk.Frame(parent, bg=C["card"]); out.pack(fill="both", expand=True)
        cv = tk.Canvas(out, bg=C["card"], highlightthickness=0)
        vs = ttk.Scrollbar(out, orient="vertical", command=cv.yview)
        inn = tk.Frame(cv, bg=C["card"])
        inn.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        win = cv.create_window((0,0), window=inn, anchor="nw")
        cv.bind("<Configure>", lambda e: cv.itemconfig(win, width=e.width))
        cv.configure(yscrollcommand=vs.set)
        cv.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")
        cv.bind("<Enter>", lambda e: cv.bind_all("<MouseWheel>",
            lambda ev: cv.yview_scroll(int(-1*(ev.delta/120)), "units")))
        cv.bind("<Leave>", lambda e: cv.unbind_all("<MouseWheel>"))
        return inn

    def _card(self, parent, title=None):
        f = tk.Frame(parent, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        f.pack(fill="x", pady=(0,12))
        inn = tk.Frame(f, bg=C["card"]); inn.pack(fill="both", expand=True, padx=18, pady=14)
        if title:
            tk.Label(inn, text=title, bg=C["card"], fg=C["accent"],
                     font=(self.ff(),12,"bold")).pack(anchor="e" if self.rtl else "w", fill="x", pady=(0,8))
        return inn

    def _build_home(self):
        a = self._scroll(self.tab_home)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,4))
        tk.Label(hd, text="🔬  " + self.t("home_w"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),18,"bold")).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("home_i"), bg=C["card"], fg=C["muted"],
                 font=(self.ff(),10), wraplength=1000).pack(anchor="w", fill="x", pady=(6,0))
        ac = self._card(a)
        tk.Label(ac, text="✎  " + self.t("author"), bg=C["card"], fg=C["gold"],
                 font=(self.ff(),11,"bold")).pack(anchor="w", fill="x")
        nm = AUTHOR_AR if self.lang=="ar" else AUTHOR_EN
        tk.Label(ac, text=nm, bg=C["card"], fg=C["text"], font=(self.ff(),12,"bold")).pack(anchor="w", fill="x")
        tk.Label(ac, text=ROLE[self.lang], bg=C["card"], fg=C["muted"]).pack(anchor="w", fill="x")
        c1 = self._card(a, "📋  " + self.t("steps"))
        for k in ("s1","s2","s3","s4","s5","s6"):
            tk.Label(c1, text="▸ " + self.t(k), bg=C["card"], fg=C["text"]).pack(anchor="w", fill="x", pady=2)
        c2 = self._card(a, "⚙  " + self.t("cond"))
        g = tk.Frame(c2, bg=C["card"]); g.pack(fill="x")
        g.columnconfigure(0, weight=0, minsize=220); g.columnconfigure(1, weight=1)
        rows = [(self.t("param"), self.t("value"))] + [(self.t(f"c{i}"), self.t(f"c{i}v")) for i in range(1,12)]
        for i,(t1,t2) in enumerate(rows):
            bg = C["card2"] if i==0 else (C["card"] if i%2 else C["bg2"])
            fg1 = C["primary"] if i==0 else C["text"]
            fnt = (self.ff(),10,"bold") if i==0 else (self.ff(),10)
            tk.Label(g, text=t1, bg=bg, fg=fg1, font=fnt, padx=10, pady=6, anchor="w").grid(
                row=i, column=0, sticky="ew", padx=(0,1), pady=1)
            tk.Label(g, text=t2, bg=bg, fg=fg1, font=fnt, padx=10, pady=6, anchor="w").grid(
                row=i, column=1, sticky="ew", pady=1)
        c3 = self._card(a, "📚  " + self.t("refs"))
        tk.Label(c3, text=self.t("refstxt"), bg=C["card"], fg=C["muted"], wraplength=1000).pack(anchor="w", fill="x")
        tk.Label(c3, text=self.t("db_info", n=len(REF_DB),
                                  s=sum(len(v) for v in SYNONYMS.values())),
                 bg=C["card"], fg=C["primary"], font=(self.ff(),11,"bold")).pack(anchor="w", fill="x", pady=(8,0))
        wf = tk.Frame(a, bg="#3b1d1d", highlightbackground=C["err"], highlightthickness=1)
        wf.pack(fill="x", padx=20, pady=(0,20))
        wi = tk.Frame(wf, bg="#3b1d1d"); wi.pack(fill="x", padx=18, pady=14)
        tk.Label(wi, text=self.t("warn"), bg="#3b1d1d", fg=C["err"],
                 font=(self.ff(),12,"bold")).pack(anchor="w", fill="x")
        tk.Label(wi, text=self.t("warntxt"), bg="#3b1d1d", fg="#fecaca", wraplength=1000).pack(anchor="w", fill="x")

    def _build_kri(self):
        a = self._scroll(self.tab_kri)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,6))
        tk.Label(hd, text="🧮  " + self.t("k_title"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),17,"bold")).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("k_sub"), bg=C["card"], fg=C["muted"]).pack(anchor="w", fill="x")
        c1 = self._card(a)
        r = tk.Frame(c1, bg=C["card"]); r.pack(fill="x", pady=(4,10))
        tk.Label(r, text=self.t("k_rt"), bg=C["card"], fg=C["text"]).pack(side="left")
        self.kri_rt = tk.StringVar()
        e = ttk.Entry(r, textvariable=self.kri_rt, width=16); e.pack(side="left", padx=8)
        e.bind("<Return>", lambda _: self._calc_kri())
        ttk.Button(r, text=self.t("k_calc"), style="Accent.TButton",
                   command=self._calc_kri).pack(side="left")
        res = tk.Frame(c1, bg=C["bg2"], highlightbackground=C["primary"], highlightthickness=1)
        res.pack(fill="x", pady=(6,4))
        self.kri_big = tk.Label(res, text="—", bg=C["bg2"], fg=C["primary"], font=(self.ff(),30,"bold"))
        self.kri_big.pack(pady=(10,0))
        tk.Label(res, text=self.t("k_result"), bg=C["bg2"], fg=C["muted"]).pack()
        self.kri_det = tk.Label(res, text="", bg=C["bg2"], fg=C["muted"])
        self.kri_det.pack(pady=(0,10))
        c2 = self._card(a, "⚡  " + self.t("k_batch"))
        self.kri_batch = tk.Text(c2, height=6, bg=C["bg2"], fg=C["text"],
                                 insertbackground=C["primary"], relief="flat",
                                 font=("Consolas",10))
        self.kri_batch.pack(fill="x")
        ttk.Button(c2, text=self.t("k_batchbtn"), style="Accent.TButton",
                   command=self._calc_batch).pack(anchor="w", pady=(10,0))
        self.kri_out = tk.Text(c2, height=6, bg=C["bg2"], fg=C["accent"],
                               relief="flat", font=("Consolas",10), state="disabled")
        self.kri_out.pack(fill="x", pady=(10,0))

    def _calc_kri(self):
        try: rt = float(self.kri_rt.get().strip().replace(",", "."))
        except ValueError:
            messagebox.showwarning(self.t("warning"), self.t("k_nofill")); return
        r = kri_from_rt(rt, self.alkanes)
        if r is None:
            self.kri_big.config(text="—", fg=C["err"]); self.kri_det.config(text=self.t("k_none")); return
        self.kri_big.config(text=f"{r[0]:.1f}", fg=C["primary"])
        self.kri_det.config(text=f"{self.t('k_before')}: C{r[1]} • {self.t('k_after')}: C{r[2]}")

    def _calc_batch(self):
        out = []
        for l in [x.strip() for x in self.kri_batch.get("1.0","end").splitlines() if x.strip()]:
            try: rt = float(l.replace(",", "."))
            except ValueError: out.append(f"{l} → ?"); continue
            r = kri_from_rt(rt, self.alkanes)
            out.append(f"{rt:.4f} → {r[0]:.1f}" if r else f"{rt:.4f} → —")
        self.kri_out.config(state="normal"); self.kri_out.delete("1.0","end")
        self.kri_out.insert("1.0", "\n".join(out)); self.kri_out.config(state="disabled")

    def _build_ak(self):
        a = self._scroll(self.tab_ak)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,6))
        tk.Label(hd, text="⛽  " + self.t("ak_title"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),17,"bold")).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("ak_sub"), bg=C["card"], fg=C["muted"]).pack(anchor="w", fill="x")
        body = tk.Frame(a, bg=C["card"]); body.pack(fill="both", expand=True, padx=20, pady=(10,20))
        form = tk.Frame(body, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        form.pack(side="left", fill="y", padx=(0,12))
        fi = tk.Frame(form, bg=C["card"]); fi.pack(padx=16, pady=16)
        tk.Label(fi, text=self.t("ak_c"), bg=C["card"], fg=C["text"]).pack(anchor="w")
        self.ak_c = tk.StringVar(); ttk.Entry(fi, textvariable=self.ak_c, width=18).pack(fill="x", pady=(2,10))
        tk.Label(fi, text=self.t("ak_rt"), bg=C["card"], fg=C["text"]).pack(anchor="w")
        self.ak_rt = tk.StringVar(); ttk.Entry(fi, textvariable=self.ak_rt, width=18).pack(fill="x", pady=(2,14))
        for txt,sty,cmd in [(self.t("ak_add"),"Accent.TButton",self._ak_add),
                            (self.t("ak_del"),"TButton",self._ak_del),
                            (self.t("ak_load"),"TButton",self._ak_load),
                            (self.t("ak_clear"),"Danger.TButton",self._ak_clear)]:
            ttk.Button(fi, text=txt, style=sty, command=cmd).pack(fill="x", pady=3)
        self.ak_cnt = tk.Label(fi, text="", bg=C["card"], fg=C["muted"]); self.ak_cnt.pack(pady=(12,0))
        right = tk.Frame(body, bg=C["card"]); right.pack(side="left", fill="both", expand=True)
        tk.Label(right, text=self.t("ak_hint"), bg=C["card"], fg=C["muted"]).pack(anchor="w", pady=(0,6))
        wrap = tk.Frame(right, bg=C["card"]); wrap.pack(fill="both", expand=True)
        self.ak_tree = ttk.Treeview(wrap, columns=("c","rt"), show="headings", height=16)
        self.ak_tree.heading("c", text=self.t("ak_c")); self.ak_tree.heading("rt", text=self.t("ak_rt"))
        self.ak_tree.column("c", width=140, anchor="center"); self.ak_tree.column("rt", width=180, anchor="center")
        vs = ttk.Scrollbar(wrap, orient="vertical", command=self.ak_tree.yview)
        self.ak_tree.configure(yscrollcommand=vs.set)
        self.ak_tree.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")
        self.ak_tree.bind("<Double-1>", self._ak_edit); self._ak_refresh()

    def _ak_refresh(self):
        self.ak_tree.delete(*self.ak_tree.get_children())
        for c,rt in sorted(self.alkanes):
            self.ak_tree.insert("", "end", values=(f"C{c}", f"{rt:.2f}"))
        self.ak_cnt.config(text=f"{self.t('ak_cnt')} {len(self.alkanes)}")

    def _ak_add(self):
        try:
            c = int(float(self.ak_c.get().replace(",", ".")))
            rt = float(self.ak_rt.get().replace(",", "."))
        except ValueError:
            messagebox.showwarning(self.t("warning"), "C / RT ?"); return
        self.alkanes = [a for a in self.alkanes if a[0] != c]
        self.alkanes.append((c, rt)); self._ak_refresh()
        self.ak_c.set(""); self.ak_rt.set("")

    def _ak_del(self):
        for s in self.ak_tree.selection():
            c = int(self.ak_tree.item(s, "values")[0].replace("C",""))
            self.alkanes = [a for a in self.alkanes if a[0] != c]
        self._ak_refresh()

    def _ak_clear(self):
        if messagebox.askyesno(self.t("warning"), self.t("ak_clear") + " ?"):
            self.alkanes = []; self._ak_refresh()

    def _ak_load(self):
        self.alkanes = list(DEFAULT_ALKANES); self._ak_refresh()
        messagebox.showinfo(self.t("ok"), self.t("ak_loaded", n=len(self.alkanes)))

    def _ak_edit(self, _):
        s = self.ak_tree.selection()
        if not s: return
        v = self.ak_tree.item(s[0], "values")
        self.ak_c.set(v[0].replace("C","")); self.ak_rt.set(v[1])

    def _build_id(self):
        a = self._scroll(self.tab_id)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,6))
        tk.Label(hd, text="🔍  " + self.t("i_title"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),17,"bold")).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("i_sub"), bg=C["card"], fg=C["muted"],
                 wraplength=1100).pack(anchor="w", fill="x", pady=(4,0))
        body = tk.Frame(a, bg=C["card"]); body.pack(fill="both", expand=True, padx=20, pady=(10,20))
        form = tk.Frame(body, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        form.pack(side="left", fill="y", padx=(0,12))
        fi = tk.Frame(form, bg=C["card"]); fi.pack(padx=16, pady=16)
        def fld(lbl, var):
            tk.Label(fi, text=lbl, bg=C["card"], fg=C["text"]).pack(anchor="w")
            ttk.Entry(fi, textvariable=var, width=22).pack(fill="x", pady=(2,10))
        self.i_name = tk.StringVar(); self.i_rt = tk.StringVar(); self.i_kril = tk.StringVar()
        fld(self.t("i_name"), self.i_name); fld(self.t("i_rt"), self.i_rt); fld(self.t("i_kril"), self.i_kril)
        tk.Label(fi, text=self.t("i_match_all"), bg=C["card"], fg=C["gold"],
                 font=(self.ff(),10,"bold")).pack(anchor="w", pady=(4,4))
        self.i_match_panel = tk.Frame(fi, bg=C["bg2"]); self.i_match_panel.pack(fill="x", pady=(0,10))
        self.i_match_labels = {}
        for k in REF_KEYS:
            row = tk.Frame(self.i_match_panel, bg=C["bg2"]); row.pack(fill="x")
            tk.Label(row, text=f"{k}:", bg=C["bg2"], fg=C["muted"],
                     font=(self.ff(),9,"bold"), width=6).pack(side="left", padx=(6,2), pady=2)
            lbl = tk.Label(row, text="—", bg=C["bg2"], fg=C["muted"], font=(self.ff(),10,"bold"))
            lbl.pack(side="left", padx=2, pady=2, fill="x", expand=True)
            self.i_match_labels[k] = lbl
        self.i_rt.trace_add("write", lambda *_: self._id_auto_match())
        self.i_kril.trace_add("write", lambda *_: self._id_auto_match())
        self.i_name.trace_add("write", lambda *_: self._id_auto_match())
        for txt,sty,cmd in [(self.t("i_from_db"),"Accent.TButton",self._id_suggest),
                            (self.t("i_add"),"Accent.TButton",self._id_add),
                            (self.t("i_del"),"TButton",self._id_del),
                            (self.t("i_example"),"TButton",self._id_example),
                            (self.t("i_clear"),"Danger.TButton",self._id_clear)]:
            ttk.Button(fi, text=txt, style=sty, command=cmd).pack(fill="x", pady=3)
        self.i_sum = tk.Label(fi, text="", bg=C["card"], fg=C["muted"], wraplength=250)
        self.i_sum.pack(pady=(12,0), fill="x")
        right = tk.Frame(body, bg=C["card"]); right.pack(side="left", fill="both", expand=True)
        wrap = tk.Frame(right, bg=C["card"]); wrap.pack(fill="both", expand=True)
        cols = ("n","comp","rt","kc","kl","m","r","st")
        self.i_tree = ttk.Treeview(wrap, columns=cols, show="headings", height=14)
        for k,txt,w in [("n",self.t("ihn"),40),("comp",self.t("ihc"),220),("rt",self.t("ihrt"),80),
                        ("kc",self.t("ihkc"),90),("kl",self.t("ihl"),90),("m",self.t("ihm"),90),
                        ("r",self.t("ihr"),70),("st",self.t("ihs"),110)]:
            self.i_tree.heading(k, text=txt); self.i_tree.column(k, width=w, anchor="center")
        vs = ttk.Scrollbar(wrap, orient="vertical", command=self.i_tree.yview)
        self.i_tree.configure(yscrollcommand=vs.set)
        self.i_tree.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")
        self.i_tree.tag_configure("ok", background="#14351f", foreground="#86efac")
        self.i_tree.tag_configure("tent", background="#3b2f10", foreground="#fcd34d")
        self.i_tree.tag_configure("unk", background="#3b1414", foreground="#fca5a5")
        self.i_tree.bind("<Double-1>", self._id_edit)
        self._id_refresh()

    def _id_auto_match(self):
        for k in REF_KEYS: self.i_match_labels[k].config(text="—", fg=C["muted"])
        rt_s = self.i_rt.get().strip().replace(",", ".")
        if not rt_s: return
        try: rt = float(rt_s)
        except ValueError: return
        res = kri_from_rt(rt, self.alkanes)
        if res is None: return
        kc = res[0]
        kl_s = self.i_kril.get().strip().replace(",", ".")
        kl = None
        if kl_s:
            try: kl = float(kl_s)
            except ValueError: pass
        name = self.i_name.get().strip()
        row = find_canonical(name) if name else None
        if row is not None:
            m = match_all(kc, row)
            for k in REF_KEYS:
                val, mp = m[k]
                if mp is None: self.i_match_labels[k].config(text="—", fg=C["muted"])
                else:
                    col = C["ok"] if mp >= 80 else (C["gold"] if mp >= 60 else C["err"])
                    self.i_match_labels[k].config(text=f"{mp:5.1f}%   (KRI_ref={val:.1f})", fg=col)
        elif kl is not None:
            mp = match_percent(kc, kl)
            col = C["ok"] if mp >= 80 else (C["gold"] if mp >= 60 else C["err"])
            for k in REF_KEYS:
                self.i_match_labels[k].config(text=f"{mp:5.1f}%   (KRI_ref={kl:.1f})", fg=col)
        else:
            cands = find_best_candidates(kc, 30)
            if cands:
                r0 = cands[0][0]
                m = match_all(kc, r0)
                for k in REF_KEYS:
                    val, mp = m[k]
                    if mp is None: self.i_match_labels[k].config(text="—", fg=C["muted"])
                    else:
                        col = C["ok"] if mp >= 80 else (C["gold"] if mp >= 60 else C["err"])
                        self.i_match_labels[k].config(text=f"{mp:5.1f}%   (KRI_ref={val:.1f})", fg=col)

    def _id_suggest(self):
        dlg = tk.Toplevel(self); dlg.title(self.t("ref_title"))
        dlg.configure(bg=C["bg"]); dlg.geometry("1150x640")
        dlg.transient(self); dlg.grab_set()
        top = tk.Frame(dlg, bg=C["bg2"]); top.pack(fill="x")
        tk.Label(top, text=self.t("ref_search"), bg=C["bg2"], fg=C["text"]).pack(side="left", padx=(12,4), pady=8)
        sv = tk.StringVar(value=self.i_name.get().strip())
        e = ttk.Entry(top, textvariable=sv, width=40); e.pack(side="left", fill="x", expand=True, padx=4, pady=8)
        cur_kc = None; rt_val = None
        try:
            rt_val = float(self.i_rt.get().replace(",", "."))
            r = kri_from_rt(rt_val, self.alkanes)
            if r: cur_kc = r[0]
        except: pass
        info = tk.Label(top, text="", bg=C["bg2"], fg=C["gold"])
        info.pack(side="right", padx=12)
        info.config(text=f"RT={rt_val:.4f} → KRI={cur_kc:.1f}" if cur_kc is not None
                    else self.t("ref_nort"), fg=C["gold"] if cur_kc else C["muted"])
        w = tk.Frame(dlg, bg=C["bg"]); w.pack(fill="both", expand=True, padx=12, pady=8)
        cols = ("n","cas","d1","m1","d5","m5","peg","mpeg","a","ma","best")
        tree = ttk.Treeview(w, columns=cols, show="headings")
        for k,txt,wd in [("n",self.t("rhn"),220),("cas",self.t("rhcas"),95),
                         ("d1","KRI DB-1",70),("m1","%DB-1",60),("d5","KRI DB-5",70),("m5","%DB-5",60),
                         ("peg","KRI PEG",70),("mpeg","%PEG",60),("a","KRI Adams",70),("ma","%Adams",60),
                         ("best","Best",80)]:
            tree.heading(k, text=txt); tree.column(k, width=wd, anchor="center")
        vs = ttk.Scrollbar(w, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vs.set)
        tree.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")
        tree.tag_configure("ok", background="#14351f", foreground="#86efac")
        tree.tag_configure("good", background="#1a3a2a", foreground="#a7f3d0")
        tree.tag_configure("tent", background="#3b2f10", foreground="#fcd34d")
        tree.tag_configure("unk", background="#3b1414", foreground="#fca5a5")
        def fmt(v): return f"{v:.1f}" if v is not None else "—"
        def fmp(m): return f"{m:.1f}" if m is not None else "—"
        def fill():
            tree.delete(*tree.get_children())
            rows = search_ref(sv.get())
            if cur_kc is not None:
                rows = sorted(rows, key=lambda r: -(best_match(cur_kc, r)[2] if best_match(cur_kc, r) else -1))
            for r in rows:
                m = match_all(cur_kc, r) if cur_kc is not None else \
                    {k:(v, None) for k,v in zip(REF_KEYS, (r[3],r[4],r[5],r[6]))}
                b = best_match(cur_kc, r) if cur_kc is not None else None
                best_str = f"{b[2]:.1f} ({b[0]})" if b else "—"
                tag = ""
                if b:
                    if b[2] >= 90: tag = "ok"
                    elif b[2] >= 80: tag = "good"
                    elif b[2] >= 60: tag = "tent"
                    else: tag = "unk"
                tree.insert("", "end", tags=(tag,), values=(
                    r[0], r[1], fmt(r[3]), fmp(m["DB-1"][1]), fmt(r[4]), fmp(m["DB-5"][1]),
                    fmt(r[5]), fmp(m["PEG"][1]), str(r[6]) if r[6] is not None else "—",
                    fmp(m["Adams"][1]), best_str))
        fill(); sv.trace_add("write", lambda *_: fill())
        def use():
            s = tree.selection()
            if not s: return
            v = tree.item(s[0], "values")
            self.i_name.set(v[0])
            if v[4] != "—": self.i_kril.set(v[4])
            self._id_auto_match(); dlg.destroy()
        bf = tk.Frame(dlg, bg=C["bg"]); bf.pack(fill="x", padx=12, pady=(0,12))
        ttk.Button(bf, text=self.t("ref_use"), style="Accent.TButton", command=use).pack(side="right")
        ttk.Button(bf, text=self.t("cancel"), command=dlg.destroy).pack(side="right", padx=(0,8))
        tree.bind("<Double-1>", lambda _: use()); e.focus_set()

    def _id_add(self):
        n = self.i_name.get().strip()
        if not n: return
        try: rt = float(self.i_rt.get().replace(",", "."))
        except ValueError:
            messagebox.showwarning(self.t("warning"), self.t("i_rt")); return
        kl_s = self.i_kril.get().strip().replace(",", ".")
        if not kl_s:
            res = kri_from_rt(rt, self.alkanes); kc = res[0] if res else None
            cands = find_best_candidates(kc, 30) if kc else []
            if not cands: messagebox.showwarning(self.t("warning"), self.t("k_none")); return
            kl = cands[0][2]; self.i_kril.set(f"{kl:.1f}")
        else:
            try: kl = float(kl_s)
            except ValueError: messagebox.showwarning(self.t("warning"), self.t("i_kril")); return
        res = kri_from_rt(rt, self.alkanes); kc = res[0] if res else None
        mp = match_percent(kc, kl) if kc is not None else 0.0
        self.ident_rows.append({"name":n,"rt":rt,"kril":kl,"match":mp})
        for v in (self.i_name, self.i_rt, self.i_kril): v.set("")
        self._id_refresh()

    def _id_del(self):
        idx = sorted((int(self.i_tree.item(s,"values")[0])-1 for s in self.i_tree.selection()), reverse=True)
        for i in idx:
            if 0 <= i < len(self.ident_rows): del self.ident_rows[i]
        self._id_refresh()

    def _id_clear(self): self.ident_rows = []; self._id_refresh()

    def _id_example(self):
        self.ident_rows = []
        for n,rt,kl in EXAMPLE_IDENT:
            row = find_canonical(n); res = kri_from_rt(rt, self.alkanes)
            kc = res[0] if res else None
            if row and kc:
                b = best_match(kc, row)
                if b:
                    self.ident_rows.append({"name":n,"rt":rt,"kril":b[1],"match":b[2]}); continue
            mp = match_percent(kc, kl) if kc is not None else 0.0
            self.ident_rows.append({"name":n,"rt":rt,"kril":kl,"match":mp})
        self._id_refresh()

    def _id_edit(self, _):
        s = self.i_tree.selection()
        if not s: return
        v = self.i_tree.item(s[0], "values")
        self.i_name.set(v[1]); self.i_rt.set(v[2]); self.i_kril.set(v[4])
        self._id_auto_match()

    def _id_refresh(self):
        self.i_tree.delete(*self.i_tree.get_children())
        ok = tent = unk = 0
        for i, r in enumerate(self.ident_rows, 1):
            res = kri_from_rt(r["rt"], self.alkanes); kc = res[0] if res else None
            row = find_canonical(r["name"])
            if row and kc:
                b = best_match(kc, row); ref_key, ref_val, mp = b
            else:
                mp = match_percent(kc, r["kril"]) if kc is not None else None
                ref_key, ref_val = "DB-5", r["kril"]
            d = abs(kc - ref_val) if (kc is not None and ref_val is not None) else None
            if kc is None or mp is None: stat, tag = self.t("i_unk"), "unk"; unk += 1
            elif mp >= 80 and d <= 10: stat, tag = "✓ " + self.t("i_ok"), "ok"; ok += 1
            elif mp >= 60 and d <= 20: stat, tag = "~ " + self.t("i_tent"), "tent"; tent += 1
            else: stat, tag = "✗ " + self.t("i_unk"), "unk"; unk += 1
            self.i_tree.insert("", "end", tags=(tag,), values=(
                i, r["name"], f"{r['rt']:.4f}", f"{kc:.1f}" if kc else "—",
                f"{ref_val:.1f}" if ref_val is not None else "—",
                f"{mp:.1f}" if mp is not None else "—", ref_key, stat))
        self.i_sum.config(text=self.t("i_sum", t=len(self.ident_rows), o=ok, p=tent, u=unk))

    def _build_q(self):
        a = self._scroll(self.tab_q)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,6))
        tk.Label(hd, text="📊  " + self.t("q_title"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),17,"bold")).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("q_sub"), bg=C["card"], fg=C["muted"]).pack(anchor="w", fill="x")
        body = tk.Frame(a, bg=C["card"]); body.pack(fill="both", expand=True, padx=20, pady=(10,20))
        form = tk.Frame(body, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        form.pack(side="left", fill="y", padx=(0,12))
        fi = tk.Frame(form, bg=C["card"]); fi.pack(padx=16, pady=16)
        def fld(lbl, var):
            tk.Label(fi, text=lbl, bg=C["card"], fg=C["text"]).pack(anchor="w")
            ttk.Entry(fi, textvariable=var, width=22).pack(fill="x", pady=(2,10))
        self.q_name = tk.StringVar(); self.q_area = tk.StringVar(); self.q_kri = tk.StringVar()
        fld(self.t("q_name"), self.q_name); fld(self.t("q_area"), self.q_area); fld(self.t("q_kri"), self.q_kri)
        for txt,sty,cmd in [(self.t("q_add"),"Accent.TButton",self._q_add),
                            (self.t("q_del"),"TButton",self._q_del),
                            (self.t("q_example"),"TButton",self._q_example),
                            (self.t("q_calc"),"TButton",self._q_refresh),
                            (self.t("q_clear"),"Danger.TButton",self._q_clear)]:
            ttk.Button(fi, text=txt, style=sty, command=cmd).pack(fill="x", pady=3)
        self.q_excl_s = tk.BooleanVar(value=False); self.q_excl_h = tk.BooleanVar(value=False)
        ttk.Checkbutton(fi, text=self.t("q_excl_s"), variable=self.q_excl_s,
                        command=self._q_refresh).pack(anchor="w", pady=(12,2), fill="x")
        ttk.Checkbutton(fi, text=self.t("q_excl_h"), variable=self.q_excl_h,
                        command=self._q_refresh).pack(anchor="w", fill="x")
        right = tk.Frame(body, bg=C["card"]); right.pack(side="left", fill="both", expand=True)
        wrap = tk.Frame(right, bg=C["card"]); wrap.pack(fill="both", expand=True)
        cols = ("n","comp","area","pct","kri")
        self.q_tree = ttk.Treeview(wrap, columns=cols, show="headings", height=14)
        for k,txt,w in [("n",self.t("qhn"),40),("comp",self.t("qhc"),240),
                        ("area",self.t("qha"),130),("pct",self.t("qhp"),100),("kri",self.t("qhk"),90)]:
            self.q_tree.heading(k, text=txt); self.q_tree.column(k, width=w, anchor="center")
        vs = ttk.Scrollbar(wrap, orient="vertical", command=self.q_tree.yview)
        self.q_tree.configure(yscrollcommand=vs.set)
        self.q_tree.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")
        self.q_tree.bind("<Double-1>", self._q_edit)
        self.q_total = tk.Label(right, text="", bg=C["card"], fg=C["primary"],
                                font=(self.ff(),10,"bold"))
        self.q_total.pack(fill="x", pady=(8,0)); self._q_refresh()

    def _q_add(self):
        n = self.q_name.get().strip()
        if not n: return
        try: a = float(self.q_area.get().replace(",", ".").replace(" ", ""))
        except ValueError: messagebox.showwarning(self.t("warning"), self.t("q_area")); return
        try: k = float(self.q_kri.get().replace(",", ".")) if self.q_kri.get().strip() else None
        except ValueError: k = None
        self.quant_rows.append({"name":n,"area":a,"kri":k})
        self.q_name.set(""); self.q_area.set(""); self.q_kri.set(""); self._q_refresh()

    def _q_del(self):
        idx = sorted((int(self.q_tree.item(s,"values")[0])-1 for s in self.q_tree.selection()), reverse=True)
        for i in idx:
            if 0 <= i < len(self.quant_rows): del self.quant_rows[i]
        self._q_refresh()

    def _q_clear(self): self.quant_rows = []; self._q_refresh()
    def _q_example(self):
        self.quant_rows = [{"name":n,"area":a,"kri":k} for n,a,k in EXAMPLE_QUANT]
        self._q_refresh()

    def _q_edit(self, _):
        s = self.q_tree.selection()
        if not s: return
        v = self.q_tree.item(s[0], "values")
        self.q_name.set(v[1]); self.q_area.set(v[2].replace(",",""))
        self.q_kri.set("" if v[4]=="—" else v[4])

    def _q_refresh(self):
        self.q_tree.delete(*self.q_tree.get_children())
        rows = []
        for r in self.quant_rows:
            if self.q_excl_s.get() and r["kri"] is not None and r["kri"] < 800: continue
            if self.q_excl_h.get() and r["kri"] is not None and r["kri"] > 2500: continue
            rows.append(r)
        total = sum(r["area"] for r in rows) or 1.0
        for i, r in enumerate(rows, 1):
            pct = r["area"] / total * 100.0
            self.q_tree.insert("", "end", values=(i, r["name"], f"{r['area']:,.0f}",
                f"{pct:.2f}", f"{r['kri']:.0f}" if r["kri"] is not None else "—"))
        self.q_total.config(text=self.t("q_total", t=total, n=len(rows)))

    def _build_ref(self):
        a = self._scroll(self.tab_ref)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,6))
        tk.Label(hd, text="📚  " + self.t("ref_title"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),17,"bold")).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("ref_sub"), bg=C["card"], fg=C["muted"]).pack(anchor="w", fill="x")
        tk.Label(hd, text=self.t("ref_note"), bg=C["card"], fg=C["gold"],
                 font=(self.ff(),9,"italic")).pack(anchor="w", fill="x", pady=(4,0))
        bar = tk.Frame(a, bg=C["card"]); bar.pack(fill="x", padx=20, pady=(10,4))
        tk.Label(bar, text=self.t("ref_search"), bg=C["card"], fg=C["text"]).pack(side="left", padx=(0,8))
        self.ref_q = tk.StringVar()
        se = ttk.Entry(bar, textvariable=self.ref_q, width=40); se.pack(side="left")
        self.ref_q.trace_add("write", lambda *_: self._ref_refresh())
        ttk.Button(bar, text=self.t("ref_clear"), command=lambda: self.ref_q.set("")).pack(side="left", padx=(8,0))
        ttk.Button(bar, text=self.t("ref_use"), style="Accent.TButton", command=self._ref_use).pack(side="left", padx=(8,0))
        ttk.Button(bar, text=self.t("ref_add"), command=self._ref_add_compound).pack(side="left", padx=(8,0))
        self.ref_cnt = tk.Label(a, text="", bg=C["card"], fg=C["primary"], font=(self.ff(),10,"bold"))
        self.ref_cnt.pack(fill="x", padx=20, pady=(0,8))
        wrap = tk.Frame(a, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        wrap.pack(fill="both", expand=True, padx=20, pady=(0,20))
        cols = ("name","cas","formula","dims","db5","peg","adams","syn")
        self.ref_tree = ttk.Treeview(wrap, columns=cols, show="headings", height=20)
        for k,txt,w in [("name",self.t("rhn"),200),("cas",self.t("rhcas"),105),
                        ("formula",self.t("rhf"),80),("dims",self.t("rhd1"),75),
                        ("db5",self.t("rhd5"),75),("peg",self.t("rhpeg"),75),
                        ("adams",self.t("rha"),85),("syn",self.t("rhsyn"),260)]:
            self.ref_tree.heading(k, text=txt); self.ref_tree.column(k, width=w, anchor="center")
        vs = ttk.Scrollbar(wrap, orient="vertical", command=self.ref_tree.yview)
        self.ref_tree.configure(yscrollcommand=vs.set)
        self.ref_tree.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")
        self.ref_tree.bind("<Double-1>", lambda _: self._ref_use())
        self._ref_refresh()

    def _ref_refresh(self):
        self.ref_tree.delete(*self.ref_tree.get_children())
        rows = search_ref(self.ref_q.get())
        for r in rows:
            syns = SYNONYMS.get(r[0], [])
            syn_str = ", ".join(syns[:3]) + (f" (+{len(syns)-3})" if len(syns) > 3 else "")
            self.ref_tree.insert("", "end", values=(
                r[0], r[1], r[2],
                f"{r[3]:.1f}" if r[3] is not None else "—",
                f"{r[4]:.1f}" if r[4] is not None else "—",
                f"{r[5]:.1f}" if r[5] is not None else "—",
                str(r[6]) if r[6] is not None else "—", syn_str or "—"))
        self.ref_cnt.config(text=self.t("ref_cnt", n=len(rows), t=len(REF_DB)))

    def _ref_use(self):
        s = self.ref_tree.selection()
        if not s: return
        v = self.ref_tree.item(s[0], "values")
        kri_val = v[4] if v[4] != "—" else ""
        self.nb.select(self.tab_id)
        self.i_name.set(v[0]); self.i_kril.set(kri_val); self.i_rt.set("")
        self._id_auto_match()

    def _ref_add_compound(self):
        dlg = tk.Toplevel(self); dlg.title(self.t("ref_new_title"))
        dlg.configure(bg=C["bg"]); dlg.geometry("520x680")
        dlg.transient(self); dlg.grab_set()
        f = tk.Frame(dlg, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        f.pack(fill="both", expand=True, padx=16, pady=16)
        fi = tk.Frame(f, bg=C["card"]); fi.pack(fill="both", expand=True, padx=16, pady=16)
        fields = [("name",self.t("ref_name")),("cas",self.t("ref_cas")),
                  ("formula",self.t("ref_formula")),("db1",self.t("ref_db1")),
                  ("db5",self.t("ref_db5")),("peg",self.t("ref_peg")),
                  ("adams",self.t("ref_adams")),("syn",self.t("ref_syn"))]
        vars = {}
        for key, lbl in fields:
            tk.Label(fi, text=lbl, bg=C["card"], fg=C["text"]).pack(anchor="w")
            v = tk.StringVar(); vars[key] = v
            ttk.Entry(fi, textvariable=v, width=40).pack(fill="x", pady=(2,8))
        def save():
            name = vars["name"].get().strip()
            if not name: messagebox.showwarning(self.t("warning"), self.t("ref_name")); return
            cas = vars["cas"].get().strip() or "—"; formula = vars["formula"].get().strip() or "—"
            def num(k):
                s = vars[k].get().strip().replace(",", ".")
                if not s: return None
                try: return float(s)
                except: return None
            REF_DB.append((name, cas, formula, num("db1"), num("db5"), num("peg"), num("adams")))
            syns_txt = vars["syn"].get().strip()
            if syns_txt:
                sl = [s.strip() for s in syns_txt.split(",") if s.strip()]
                SYNONYMS.setdefault(name, []).extend(sl)
                for s in sl: _SYN_REV.setdefault(s.lower(), []).append(name)
            dlg.destroy(); self._ref_refresh()
            messagebox.showinfo(self.t("ok"), self.t("ref_saved"))
        bf = tk.Frame(fi, bg=C["card"]); bf.pack(fill="x", pady=(8,0))
        ttk.Button(bf, text=self.t("ok"), style="Accent.TButton", command=save).pack(side="right")
        ttk.Button(bf, text=self.t("cancel"), command=dlg.destroy).pack(side="right", padx=(0,8))

    def _build_rep(self):
        a = self._scroll(self.tab_rep)
        hd = tk.Frame(a, bg=C["card"]); hd.pack(fill="x", padx=20, pady=(18,6))
        tk.Label(hd, text="📄  " + self.t("rep_title"), bg=C["card"], fg=C["primary"],
                 font=(self.ff(),17,"bold")).pack(anchor="w", fill="x")
        top = tk.Frame(a, bg=C["card"]); top.pack(fill="x", padx=20, pady=(6,0))
        tk.Label(top, text=self.t("rep_sample"), bg=C["card"], fg=C["text"]).pack(side="left")
        ttk.Entry(top, textvariable=self.sample_name, width=32).pack(side="left", padx=(8,20))
        tk.Label(top, text=self.t("rep_analyst"), bg=C["card"], fg=C["text"]).pack(side="left")
        ttk.Entry(top, textvariable=self.analyst_name, width=28).pack(side="left", padx=(8,0))
        bar = tk.Frame(a, bg=C["card"]); bar.pack(fill="x", padx=20, pady=(10,0))
        for txt,cmd,sty in [(self.t("rep_gen"),self._rep_gen,"Accent.TButton"),
                            (self.t("rep_save"),self._rep_save,"TButton"),
                            (self.t("rep_copy"),self._rep_copy,"TButton")]:
            ttk.Button(bar, text=txt, style=sty, command=cmd).pack(side="left", padx=(0,8))
        body = tk.Frame(a, bg=C["card"]); body.pack(fill="both", expand=True, padx=20, pady=(10,20))
        self.rep_txt = tk.Text(body, bg=C["bg2"], fg=C["text"], relief="flat",
                               font=("Consolas",10), wrap="word")
        vs = ttk.Scrollbar(body, orient="vertical", command=self.rep_txt.yview)
        self.rep_txt.configure(yscrollcommand=vs.set)
        self.rep_txt.pack(side="left", fill="both", expand=True); vs.pack(side="right", fill="y")

    def _rep_gen(self):
        L = []; sep = "=" * 90
        L += [sep, "  GC-MS ESSENTIAL OIL ANALYSIS REPORT", sep]
        L.append(f"  Author : {AUTHOR_EN}")
        L.append(f"  Date   : {datetime.now():%Y-%m-%d %H:%M}")
        L.append(f"  Sample : {self.sample_name.get()}")
        L.append(f"  Analyst: {self.analyst_name.get()}")
        L += ["", "-"*90, "  1. GC-MS CONDITIONS", "-"*90]
        for i in range(1,12): L.append(f"  {self.t(f'c{i}'):<28}: {self.t(f'c{i}v')}")
        L += ["", "-"*90, "  2. ALKANE STANDARD", "-"*90]
        L.append("  " + " ".join(f"C{c}:{rt:.2f}" for c,rt in sorted(self.alkanes)))
        L += ["", "-"*90, "  3. IDENTIFICATION", "-"*90]
        L.append(f"  {'#':<4}{'Compound':<26}{'RT':>9}{'KRIc':>9}{'KRIref':>9}{'Match%':>8}{'Ref':>7} Status")
        for i, r in enumerate(self.ident_rows, 1):
            res = kri_from_rt(r["rt"], self.alkanes); kc = res[0] if res else None
            row = find_canonical(r["name"])
            if row and kc:
                b = best_match(kc, row); ref_key, ref_val, mp = b
            else:
                mp = match_percent(kc, r["kril"]) if kc else None
                ref_key, ref_val = "DB-5", r["kril"]
            d = abs(kc - ref_val) if (kc and ref_val) else None
            st = "Unknown"
            if kc is not None and mp is not None:
                if mp >= 80 and d <= 10: st = "Identified"
                elif mp >= 60 and d <= 20: st = "Tentative"
            kcs = f"{kc:.1f}" if kc else "—"
            rvs = f"{ref_val:.1f}" if ref_val is not None else "—"
            mps = f"{mp:.1f}" if mp is not None else "—"
            L.append(f"  {i:<4}{r['name'][:25]:<26}{r['rt']:>9.4f}{kcs:>9}{rvs:>9}{mps:>8}{ref_key:>7} {st}")
        L += ["", "-"*90, "  4. QUANTIFICATION", "-"*90]
        rows = self.quant_rows; total = sum(r["area"] for r in rows) or 1.0
        L.append(f"  {'#':<4}{'Compound':<30}{'Area':>16}{'%Area':>10}{'KRI':>8}")
        for i, r in enumerate(rows, 1):
            pct = r["area"]/total*100.0
            kris = f"{r['kri']:.0f}" if r.get("kri") is not None else "—"
            L.append(f"  {i:<4}{r['name'][:29]:<30}{r['area']:>16,.0f}{pct:>10.2f}{kris:>8}")
        L.append(f"  {'TOTAL':<34}{total:>16,.0f}{100.00:>10.2f}")
        L += ["", "-"*90, "  5. REFERENCES", "-"*90]
        L += ["  • Adams, R.P. (2017). ed. 4.1.",
              "  • Babushok et al. (2011). J. Phys. Chem. Ref. Data, 40, 043101.",
              "  • NIST WebBook", "", sep,
              "  Match % formula: 100 − |KRI_calc − KRI_ref| × 2",
              "  Acceptance: Match ≥ 80% AND |ΔKRI| ≤ 10", sep]
        self.rep_txt.delete("1.0","end"); self.rep_txt.insert("1.0", "\n".join(L))

    def _rep_save(self):
        if not self.rep_txt.get("1.0","end").strip(): self._rep_gen()
        p = filedialog.asksaveasfilename(defaultextension=".txt",
            filetypes=[("Text","*.txt")],
            initialfile=f"GCMS_report_{datetime.now():%Y%m%d_%H%M}.txt")
        if p:
            with open(p,"w",encoding="utf-8") as f: f.write(self.rep_txt.get("1.0","end"))
            messagebox.showinfo(self.t("ok"), self.t("saved"))

    def _rep_copy(self):
        if not self.rep_txt.get("1.0","end").strip(): self._rep_gen()
        self.clipboard_clear(); self.clipboard_append(self.rep_txt.get("1.0","end"))
        messagebox.showinfo(self.t("ok"), self.t("copied"))


if __name__ == "__main__":
    App().mainloop()