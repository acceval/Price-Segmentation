[![Price Segmentation](https://github.com/acceval/Price-Segmentation/actions/workflows/main.yml/badge.svg)](https://github.com/acceval/Price-Segmentation/actions/workflows/main.yml)

# Price-Segmentation

[Link to the presentation](https://docs.google.com/presentation/d/1cbuh-HAZkFPrj3fEssscG-oDuvXqo1a0rcQUDQjdgjo/edit?usp=sharing)

Price Segmentation is a price given to different segment. The key idea in this concept is the </b>segmentation</b>.

In this exercise, we segment the customers (companies) and transaction. Since the dataset is specific for 1 product family, we do not segment the product. We also the minimum segment mumbers to 3. So the final product, we should at least have 9 segmentation (3 segments from customers x 3 segments from transaction). 

![Concept](https://github.com/acceval/Price-Segmentation/blob/main/images/Price%20Segmentation.png)

## Customer Segementation

![Customer Segmentation](https://github.com/acceval/Price-Segmentation/blob/main/images/Customer%20Segmentation_.png)

![Customer Segmentation Featues](https://github.com/acceval/Price-Segmentation/blob/main/images/Customer%20Segmentation%20Radar_.png)

## Transaction Segementation

![Transaction Segmentation](https://github.com/acceval/Price-Segmentation/blob/main/images/Transaction%20Segmentation_.png)

![Transaction Segmentation Featues](https://github.com/acceval/Price-Segmentation/blob/main/images/Transaction%20Segmentation%20Radar_.png)

## Price Segmentation 


![Premium Price Price Segmentation](https://github.com/acceval/Price-Segmentation/blob/main/images/Price%20Segmentation_.png)

![Premium Price Price Segmentation Kde](https://github.com/acceval/Price-Segmentation/blob/main/images/Price%20Segmentation%20Kde_.png)

## Note

- For deployment, please refer to Price Segmentation V.4 - Deployment.ipynb. We use slightly different approach for the segmentation.
 

# Deployment

## Feature Assesment

Return parameters that picked by users along with the p-values.

### Resource URL

```
https://price-segmentation.herokuapp.com/features_assessment
```

### Parameters

```
{"filepath" :"sample_input_file.csv", "features":["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"], "target_feature":"Price_Premium"}
```

1. filepath: Path to csv file contains all the data

> Sample of the input file is [here](https://github.com/acceval/Price-Segmentation/blob/main/sample_input_file.csv). Please note that column names cannot contain space.

2. features: List of features

> List of column name that users want to use to segment the data. Each feature should exist as a column name and cannot contain space. Currently, features cannot be date data.

3. target: Target feature

> Feature that aim to be used as reference for segmentation. In this sample data, the target feature is "Price Premium".

### How To Call

```
curl -X POST -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 229' -H 'Content-type: application/json' -H 'User-Agent: python-requests/2.26.0' -d '{"filepath" :"sample_input_file.csv", "features":["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"], "target_feature":"Price_Premium"}' https://price-segmentation.herokuapp.com/features_assessment
```

### Sample Output

```
{"status": 1, "error": null, "data": "{\"Customer_Type\": 0.0, \"Customer_Industry\": 0.0, \"Grade\": 0.435, \"Country\": 0.0, \"Destination_Port\": 0.0, \"City_State\": 0.301, \"Shipping_Condition\": 0.0, \"Export/Domestic\": 0.0, \"QUANTITY\": 0.0}"}
```

## Segmentation

### Resource URL

```
https://price-segmentation.herokuapp.com/segmentation
```

### Parameters

```
{"filepath" :"sample_input_file.csv", "features":["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"], "target_feature":"Price_Premium","index":"Index"}
```

Input:

1. filepath: Path to csv file contains all the data

> Sample of the input file is [here](https://github.com/acceval/Price-Segmentation/blob/main/sample_input_file.csv). Please note that column names cannot contain space.

2. features: List of features

> List of column name that users want to use to segment the data. Each feature should exist as a column name and cannot contain space. Currently, features cannot be date data.

3. target: Target feature

> Feature that aim to be used as reference for segmentation. In this sample data, the target feature is "Price Premium".

4. index: Index column 

> Index acts like acts like a primary key in a database table. Values in this column should be unique.  

5. max_depth: optional, default value is 3  

> This is the parameter on how far the segmentation goes.

6. min_samples_leaf: optional, default value is 100.  

> This is the parameter that ensure minimum number of sample per segment.

### How To Call

```
curl -X POST -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 245' -H 'Content-type: application/json' -H 'User-Agent: python-requests/2.26.0' -d '{"filepath" :"sample_input_file.csv", "features":["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"], "target_feature":"Price_Premium","index":"Index"}' https://price-segmentation.herokuapp.com/segmentation
```

### Sample Output

```
{"status": 1, "error": null, "data": [{"segment": 0, "Index": [16, 29, 33, 38, 73, 84, 87, 100, 101, 105, 115, 120, 124, 133, 135, 140, 151, 169, 180, 186, 227, 246, 253, 259, 296, 297, 304, 306, 314, 316, 327, 339, 340, 352, 354, 407, 437, 441, 446, 452, 470, 478, 483, 487, 517, 536, 574, 591, 593, 606, 615, 654, 661, 673, 680, 694, 699, 716, 727, 734, 736, 742, 746, 748, 758, 765, 771, 819, 847, 894, 905, 918, 919, 932, 942, 957, 996, 1001, 1012, 1013, 1038, 1041, 1046, 1049, 1058, 1068, 1072, 1082, 1115, 1127, 1135, 1145, 1166, 1171, 1179, 1183, 1189, 1196, 1206, 1208, 1218, 1222, 1228, 1244, 1255, 1266, 1274, 1283, 1287, 1339, 1343, 1345, 1347, 1371, 1372, 1373, 1377, 1391, 1396, 1435, 1436, 1437, 1442, 1460, 1463, 1467, 1472, 1489, 1495, 1503, 1505, 1510, 1534, 1570, 1572, 1583, 1615, 1618, 1647, 1655, 1657, 1664, 1691, 1693, 1696, 1719, 1724, 1732, 1749, 1750, 1751, 1764, 1815]}, {"segment": 1, "Index": [2, 6, 13, 19, 20, 28, 39, 47, 49, 55, 60, 62, 69, 70, 72, 76, 77, 85, 88, 90, 95, 96, 102, 103, 107, 111, 113, 131, 137, 141, 144, 145, 150, 154, 157, 159, 160, 161, 164, 176, 179, 190, 191, 196, 199, 204, 205, 207, 208, 216, 217, 218, 222, 223, 224, 225, 231, 236, 240, 244, 245, 248, 250, 260, 269, 271, 278, 286, 287, 294, 295, 298, 303, 319, 320, 321, 322, 323, 324, 329, 330, 332, 337, 349, 350, 355, 356, 361, 366, 367, 369, 371, 372, 373, 374, 380, 391, 392, 400, 402, 411, 418, 419, 423, 432, 433, 435, 438, 439, 445, 447, 448, 453, 459, 460, 461, 462, 463, 464, 466, 469, 472, 481, 482, 488, 490, 491, 492, 493, 507, 512, 513, 514, 515, 516, 518, 521, 526, 532, 541, 542, 547, 548, 558, 561, 563, 565, 569, 572, 573, 576, 577, 579, 580, 581, 595, 596, 599, 601, 603, 608, 612, 613, 614, 620, 630, 633, 635, 637, 639, 641, 643, 644, 649, 653, 657, 660, 662, 663, 664, 666, 668, 671, 677, 678, 679, 685, 686, 687, 689, 691, 693, 695, 696, 704, 717, 718, 721, 730, 737, 743, 757, 759, 760, 761, 770, 779, 784, 788, 790, 794, 797, 805, 806, 807, 813, 816, 817, 820, 825, 827, 832, 835, 839, 842, 845, 851, 852, 853, 860, 861, 863, 874, 876, 877, 878, 880, 885, 886, 887, 891, 896, 898, 900, 909, 911, 921, 922, 928, 929, 930, 935, 953, 963, 968, 969, 976, 980, 981, 983, 987, 990, 993, 995, 1005, 1007, 1016, 1021, 1024, 1025, 1027, 1031, 1036, 1037, 1040, 1042, 1048, 1056, 1057, 1059, 1065, 1071, 1077, 1081, 1085, 1086, 1088, 1091, 1092, 1093, 1095, 1097, 1104, 1107, 1109, 1112, 1114, 1116, 1121, 1122, 1124, 1126, 1128, 1133, 1134, 1136, 1140, 1152, 1154, 1158, 1159, 1161, 1164, 1165, 1169, 1172, 1175, 1176, 1194, 1195, 1204, 1214, 1220, 1231, 1235, 1236, 1237, 1242, 1251, 1264, 1265, 1268, 1271, 1279, 1281, 1282, 1286, 1289, 1293, 1294, 1295, 1298, 1303, 1304, 1307, 1308, 1309, 1311, 1312, 1314, 1316, 1317, 1319, 1321, 1322, 1323, 1326, 1327, 1328, 1330, 1336, 1342, 1348, 1349, 1354, 1356, 1358, 1360, 1362, 1363, 1376, 1380, 1385, 1389, 1393, 1394, 1395, 1399, 1403, 1404, 1407, 1408, 1414, 1432, 1433, 1434, 1438, 1440, 1447, 1454, 1459, 1466, 1471, 1477, 1492, 1493, 1497, 1499, 1506, 1511, 1513, 1516, 1521, 1523, 1525, 1526, 1529, 1531, 1538, 1545, 1546, 1549, 1552, 1558, 1559, 1561, 1562, 1573, 1574, 1575, 1577, 1578, 1579, 1580, 1585, 1591, 1594, 1596, 1597, 1599, 1604, 1610, 1611, 1612, 1613, 1614, 1616, 1617, 1620, 1622, 1634, 1645, 1646, 1649, 1652, 1658, 1672, 1673, 1674, 1676, 1677, 1686, 1687, 1694, 1701, 1706, 1708, 1713, 1720, 1721, 1725, 1728, 1731, 1736, 1740, 1741, 1747, 1752, 1757, 1758, 1762, 1766, 1767, 1768, 1771, 1772, 1784, 1785, 1786, 1787, 1788, 1789, 1792, 1796, 1798, 1800, 1801, 1802, 1805, 1806, 1807, 1811, 1812, 1817]}, {"segment": 2, "Index": [4, 14, 25, 32, 44, 48, 54, 71, 91, 132, 134, 136, 155, 156, 166, 167, 171, 197, 206, 270, 274, 277, 281, 300, 305, 331, 333, 344, 346, 347, 348, 379, 383, 415, 458, 471, 479, 503, 528, 544, 545, 546, 554, 556, 557, 605, 619, 627, 676, 700, 731, 732, 756, 775, 778, 793, 798, 800, 801, 812, 815, 822, 830, 841, 864, 875, 895, 903, 906, 910, 934, 939, 979, 1008, 1015, 1033, 1044, 1052, 1099, 1108, 1110, 1132, 1138, 1168, 1213, 1252, 1253, 1256, 1257, 1359, 1366, 1413, 1417, 1450, 1465, 1480, 1481, 1485, 1487, 1514, 1560, 1564, 1568, 1588, 1669, 1714, 1739, 1760, 1761, 1791]}, {"segment": 3, "Index": [3, 7, 9, 23, 26, 31, 42, 51, 56, 59, 61, 63, 66, 74, 79, 80, 81, 82, 83, 97, 99, 106, 110, 118, 119, 128, 129, 139, 146, 147, 149, 153, 162, 168, 170, 177, 178, 182, 185, 202, 211, 232, 233, 235, 237, 262, 266, 273, 275, 279, 280, 288, 292, 310, 312, 317, 318, 336, 342, 343, 353, 362, 365, 377, 378, 382, 385, 386, 396, 397, 408, 425, 428, 430, 467, 474, 485, 489, 495, 496, 499, 502, 504, 505, 519, 523, 527, 533, 534, 537, 538, 543, 551, 568, 578, 585, 586, 587, 589, 590, 598, 600, 604, 616, 621, 623, 628, 640, 645, 651, 656, 665, 684, 688, 709, 714, 722, 723, 724, 725, 728, 729, 735, 738, 739, 741, 745, 747, 750, 752, 753, 755, 767, 768, 769, 777, 781, 782, 795, 811, 818, 834, 840, 843, 850, 854, 855, 857, 873, 893, 915, 933, 938, 940, 946, 947, 949, 954, 961, 966, 967, 973, 974, 982, 984, 989, 994, 997, 998, 1010, 1011, 1029, 1039, 1050, 1051, 1054, 1055, 1061, 1062, 1066, 1074, 1094, 1111, 1118, 1139, 1141, 1143, 1150, 1151, 1155, 1156, 1173, 1174, 1181, 1187, 1188, 1192, 1197, 1198, 1200, 1201, 1205, 1212, 1215, 1225, 1232, 1241, 1243, 1248, 1249, 1254, 1258, 1262, 1263, 1273, 1277, 1278, 1280, 1284, 1290, 1299, 1300, 1302, 1310, 1325, 1332, 1333, 1357, 1364, 1365, 1367, 1370, 1379, 1382, 1386, 1387, 1400, 1401, 1406, 1411, 1415, 1418, 1426, 1428, 1431, 1439, 1443, 1444, 1445, 1449, 1457, 1468, 1469, 1476, 1484, 1496, 1498, 1500, 1501, 1502, 1504, 1509, 1528, 1532, 1535, 1537, 1544, 1548, 1551, 1555, 1567, 1576, 1589, 1598, 1600, 1628, 1631, 1633, 1635, 1637, 1638, 1639, 1640, 1641, 1642, 1648, 1651, 1653, 1661, 1662, 1663, 1665, 1666, 1670, 1671, 1683, 1689, 1697, 1698, 1705, 1710, 1717, 1726, 1727, 1729, 1730, 1753, 1754, 1755, 1759, 1763, 1774, 1778, 1782]}, {"segment": 4, "Index": [8, 17, 21, 36, 50, 52, 65, 67, 68, 92, 93, 108, 126, 130, 158, 184, 193, 212, 241, 243, 247, 284, 290, 307, 309, 334, 338, 376, 405, 409, 416, 429, 444, 455, 531, 539, 575, 582, 624, 626, 647, 652, 672, 675, 702, 703, 708, 713, 733, 773, 780, 783, 786, 787, 810, 831, 856, 872, 883, 884, 889, 907, 914, 937, 959, 986, 988, 1018, 1020, 1028, 1030, 1047, 1067, 1069, 1087, 1098, 1100, 1184, 1203, 1207, 1209, 1226, 1238, 1291, 1297, 1306, 1313, 1320, 1344, 1378, 1402, 1423, 1441, 1451, 1453, 1515, 1517, 1524, 1541, 1563, 1571, 1592, 1601, 1606, 1609, 1623, 1630, 1675, 1712, 1735, 1776, 1779, 1790]}, {"segment": 5, "Index": [1, 5, 10, 11, 12, 15, 18, 22, 24, 27, 30, 34, 35, 37, 40, 41, 43, 45, 46, 53, 57, 58, 64, 78, 86, 89, 94, 98, 104, 109, 112, 114, 116, 121, 122, 123, 125, 127, 138, 142, 143, 148, 152, 163, 165, 172, 173, 174, 175, 181, 183, 187, 188, 189, 192, 194, 195, 198, 200, 201, 203, 209, 210, 213, 214, 215, 219, 220, 221, 226, 228, 229, 230, 234, 238, 239, 242, 249, 251, 252, 254, 255, 256, 257, 258, 261, 263, 264, 265, 267, 268, 272, 276, 283, 285, 289, 291, 293, 299, 301, 302, 308, 311, 313, 315, 325, 326, 328, 335, 341, 345, 351, 357, 358, 359, 360, 363, 364, 368, 370, 375, 381, 384, 387, 388, 389, 390, 393, 394, 395, 398, 399, 401, 403, 404, 406, 410, 412, 413, 414, 417, 420, 421, 422, 424, 426, 427, 431, 434, 436, 442, 443, 449, 450, 451, 454, 456, 457, 465, 468, 473, 475, 476, 477, 480, 484, 486, 494, 497, 498, 500, 501, 506, 509, 510, 511, 520, 522, 524, 525, 529, 530, 535, 540, 549, 550, 552, 553, 555, 559, 560, 562, 564, 566, 567, 570, 571, 583, 584, 588, 592, 594, 597, 602, 607, 609, 610, 611, 617, 618, 622, 629, 631, 632, 634, 636, 638, 642, 648, 650, 655, 658, 669, 670, 674, 681, 682, 683, 690, 692, 697, 698, 701, 705, 706, 707, 710, 711, 712, 715, 719, 720, 726, 740, 744, 749, 751, 754, 762, 763, 764, 766, 772, 774, 776, 785, 789, 791, 792, 796, 799, 802, 803, 804, 808, 809, 814, 821, 823, 824, 826, 828, 829, 833, 836, 837, 844, 846, 848, 849, 858, 859, 862, 865, 866, 867, 868, 869, 870, 871, 879, 881, 882, 888, 890, 892, 897, 899, 901, 902, 904, 908, 912, 913, 916, 917, 920, 923, 924, 925, 926, 927, 931, 936, 941, 943, 944, 945, 948, 950, 951, 952, 955, 956, 958, 960, 962, 964, 965, 971, 972, 975, 977, 985, 991, 992, 999, 1000, 1002, 1006, 1009, 1014, 1017, 1019, 1022, 1023, 1026, 1032, 1034, 1035, 1043, 1045, 1053, 1060, 1063, 1064, 1070, 1073, 1075, 1076, 1078, 1079, 1080, 1083, 1084, 1089, 1090, 1096, 1101, 1102, 1103, 1105, 1106, 1113, 1117, 1119, 1120, 1123, 1125, 1129, 1130, 1131, 1137, 1142, 1144, 1146, 1147, 1148, 1149, 1153, 1157, 1160, 1162, 1163, 1167, 1170, 1178, 1180, 1182, 1185, 1186, 1191, 1193, 1199, 1202, 1210, 1211, 1216, 1217, 1219, 1221, 1223, 1224, 1227, 1229, 1230, 1233, 1234, 1239, 1240, 1245, 1246, 1247, 1250, 1260, 1261, 1267, 1269, 1270, 1272, 1275, 1276, 1285, 1288, 1292, 1296, 1301, 1305, 1315, 1318, 1324, 1329, 1331, 1334, 1335, 1337, 1338, 1340, 1341, 1346, 1350, 1351, 1352, 1353, 1355, 1361, 1368, 1369, 1374, 1375, 1381, 1383, 1384, 1388, 1390, 1392, 1397, 1398, 1405, 1409, 1410, 1412, 1416, 1419, 1420, 1421, 1422, 1424, 1425, 1429, 1430, 1446, 1448, 1452, 1455, 1456, 1458, 1461, 1462, 1464, 1470, 1473, 1474, 1475, 1478, 1479, 1482, 1483, 1486, 1488, 1490, 1491, 1494, 1507, 1508, 1512, 1518, 1519, 1520, 1522, 1527, 1530, 1533, 1536, 1539, 1540, 1542, 1543, 1547, 1550, 1553, 1554, 1556, 1557, 1565, 1566, 1581, 1582, 1584, 1586, 1587, 1590, 1593, 1595, 1602, 1603, 1605, 1607, 1608, 1619, 1621, 1624, 1625, 1626, 1627, 1629, 1632, 1643, 1644, 1650, 1654, 1656, 1659, 1667, 1668, 1678, 1679, 1680, 1681, 1682, 1684, 1685, 1688, 1690, 1692, 1695, 1699, 1700, 1702, 1703, 1707, 1709, 1711, 1715, 1716, 1718, 1722, 1723, 1733, 1734, 1737, 1738, 1742, 1743, 1744, 1745, 1746, 1748, 1756, 1765, 1769, 1770, 1773, 1775, 1777, 1780, 1781, 1783, 1793, 1795, 1797, 1799, 1803, 1804, 1808, 1809, 1813, 1814, 1816]}]}
```

## Price Segmentation

### Resource URL

```
https://price-segmentation.herokuapp.com/price_segmentation
```

### Parameters

```
{"price_per_segment" :"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json", "price_threshold":"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json", "segment":"segment","target":"Price Premium"}
```

Input:

1. price_per_segment: JSON file

> Sample of the input file is [here](https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json). 

2. price_threshold: JSON file

> Sample of the input file is [here](https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json) for standard/global setting and [here](https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold_with_power_index.json) for setting per each segment. 

3. segment: Key name for the segment

> Specify the key name for the segment from price_per_segment file.

4. target: Key name for the target

> Specify the target from price_per_segment file.

5. is_power_index: Specify whether each segment has its own threshold. True if it does, and False if it does not.  

> The parameter that specify if the price_threshold is a global config or if it config per segment. 

**Global Setting**

### How To Call

```
curl -X POST -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 268' -H 'Content-type: application/json' -H 'User-Agent: python-requests/2.26.0' -d '{"price_per_segment" :"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json", "price_threshold":"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/global_threshold.json", "segment":"segment","target":"Price Premium"}' https://price-segmentation.herokuapp.com/price_segmentation
```

```
{"status": 1, "error": null, "data": [{"segment": 0, "Price Premium": [{"floor": -117.2439732}, {"target": -62.73831199999996}, {"offer": -35.308112}]}, {"segment": 1, "Price Premium": [{"floor": -109.7022871}, {"target": -78.0353299999999}, {"offer": -52.61658969999994}]}, {"segment": 2, "Price Premium": [{"floor": -123.0680013}, {"target": -102.85694450000001}, {"offer": -95.85126260000007}]}, {"segment": 3, "Price Premium": [{"floor": -54.04887149999983}, {"target": -25.792374}, {"offer": -14.172910500000066}]}, {"segment": 4, "Price Premium": [{"floor": -22.073945599999995}, {"target": -7.451125999999949}, {"offer": -5.216719200000074}]}, {"segment": 5, "Price Premium": [{"floor": -58.42146240000001}, {"target": -22.161956}, {"offer": -6.679723599999941}]}]}
```

**Customized Setting**

### How To Call

```
curl -X POST -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 278' -H 'Content-type: application/json' -H 'User-Agent: python-requests/2.26.0' -d '{"price_per_segment" :"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json", "price_threshold":"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/customised_threshold_final.json", "segment":"segment","target":"Price Premium"}' https://price-segmentation.herokuapp.com/price_segmentation
```

### Sample Output

```
{"status": 1, "error": null, "data": [{"segment": 0, "threshold": [{"floor": -143.50034392, "target": -62.73831199999996, "offer": -33.1293080800001}]}, {"segment": 1, "threshold": [{"floor": -103.94596299999999, "target": -68.0373892500001, "offer": -51.04125}]}, {"segment": 2, "threshold": [{"floor": -151.53698607, "target": -101.8658244, "offer": -93.46905340000006}]}, {"segment": 3, "threshold": [{"floor": -89.18204996999984, "target": -25.792374, "offer": -14.172910500000066}]}, {"segment": 4, "threshold": [{"floor": -30.706449919999997, "target": -5.80580600000003, "offer": -4.323933600000028}]}, {"segment": 5, "threshold": [{"floor": -103.08434823999964, "target": -12.077351999999951, "offer": -7.827652399999973}]}]}
```

**Price Power Index Setting**

### How To Call

```
curl -X POST -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 275' -H 'Content-type: application/json' -H 'User-Agent: python-requests/2.26.0' -d '{"price_per_segment" :"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json", "price_threshold":"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_power_index_final.json", "segment":"segment","target":"Price Premium"}' https://price-segmentation.herokuapp.com/price_segmentation
```

### Sample Output

```{"status": 1, "error": null, "data": [{"segment": 0, "item": [{"price power index": "4 - 5", "threshold": [{"floor": -143.50034392, "target": -62.73831199999996, "offer": -33.1293080800001}]}, {"price power index": "3 - 4", "threshold": [{"floor": -139.23654784000001, "target": -63.36826991999993, "offer": -33.64101704000008}]}, {"price power index": "2 - 3", "threshold": [{"floor": -134.97275176, "target": -63.05329095999994, "offer": -34.19630040000005}]}, {"price power index": "1 - 2", "threshold": [{"floor": -139.23654784000001, "target": -61.716013919999995, "offer": -33.1293080800001}]}, {"price power index": "0 - 1", "threshold": [{"floor": -126.4451596, "target": -63.683248879999915, "offer": -33.64101704000008}]}]}, {"segment": 1, "item": [{"price power index": "4 - 5", "threshold": [{"floor": -137.70166718000002, "target": -78.0353299999999, "offer": -50.8079499999999}]}, {"price power index": "3 - 4", "threshold": [{"floor": -137.60467436000002, "target": -79.03145911999994, "offer": -50.842326949999915}]}, {"price power index": "2 - 3", "threshold": [{"floor": -137.60192, "target": -78.0353299999999, "offer": -51.04125}]}, {"price power index": "1 - 2", "threshold": [{"floor": -137.60467436000002, "target": -77.10434923999999, "offer": -50.8079499999999}]}, {"price power index": "0 - 1", "threshold": [{"floor": -135.74192, "target": -80.49304142999999, "offer": -50.842326949999915}]}]}, {"segment": 2, "item": [{"price power index": "4 - 5", "threshold": [{"floor": -151.53698607, "target": -102.85694450000001, "offer": -91.64181228000002}]}, {"price power index": "3 - 4", "threshold": [{"floor": -148.07397214, "target": -103.15010872, "offer": -92.55543284000005}]}, {"price power index": "2 - 3", "threshold": [{"floor": -144.61095821, "target": -103.00352661000001, "offer": -93.46905340000006}]}, {"price power index": "1 - 2", "threshold": [{"floor": -148.07397214, "target": -102.41719817, "offer": -91.64181228000002}]}, {"price power index": "0 - 1", "threshold": [{"floor": -137.68493035, "target": -103.29669083, "offer": -92.55543284000005}]}]}, {"segment": 3, "item": [{"price power index": "4 - 5", "threshold": [{"floor": -89.18204996999984, "target": -25.792374, "offer": -11.7081613099997}]}, {"price power index": "3 - 4", "threshold": [{"floor": -82.94041993999979, "target": -26.73440384, "offer": -12.910625929999833}]}, {"price power index": "2 - 3", "threshold": [{"floor": -76.69878990999972, "target": -26.26338892, "offer": -13.6040626499999}]}, {"price power index": "1 - 2", "threshold": [{"floor": -82.94041993999979, "target": -24.45675328999988, "offer": -11.7081613099997}]}, {"price power index": "0 - 1", "threshold": [{"floor": -63.91910259999999, "target": -27.703839720000005, "offer": -12.910625929999833}]}]}, {"segment": 4, "item": [{"price power index": "4 - 5", "threshold": [{"floor": -30.706449919999997, "target": -7.451125999999949, "offer": -3.600653439999995}]}, {"price power index": "3 - 4", "threshold": [{"floor": -29.82905984, "target": -7.89042135999995, "offer": -3.9668193600000126}]}, {"price power index": "2 - 3", "threshold": [{"floor": -28.951669759999998, "target": -7.670773679999949, "offer": -4.323933600000028}]}, {"price power index": "1 - 2", "threshold": [{"floor": -29.82905984, "target": -6.792182959999948, "offer": -3.600653439999995}]}, {"price power index": "0 - 1", "threshold": [{"floor": -27.1968896, "target": -8.110069039999951, "offer": -3.9668193600000126}]}]}, {"segment": 5, "item": [{"price power index": "4 - 5", "threshold": [{"floor": -103.08434823999964, "target": -22.161956, "offer": -5.53071999999997}]}, {"price power index": "3 - 4", "threshold": [{"floor": -92.08843319999951, "target": -22.836738719999918, "offer": -5.584114800000002}]}, {"price power index": "2 - 3", "threshold": [{"floor": -82.7002747999998, "target": -22.58583535999998, "offer": -5.853832400000018}]}, {"price power index": "1 - 2", "threshold": [{"floor": -92.08843319999951, "target": -18.573540479999707, "offer": -5.53071999999997}]}, {"price power index": "0 - 1", "threshold": [{"floor": -74.39361000000078, "target": -23.054883839999942, "offer": -5.584114800000002}]}]}]}
```






