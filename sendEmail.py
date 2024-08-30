import pandas as pd

df = pd.read_excel('studentListInCourse-20240830.xls')
student_id = df['学号'].tolist()

sent_id = {
    1900012178, 2000013361, 2000013372, 2100011745, 2100011800, 2100013281, 2100013359, 2100013383, 2100014523, 2100015521,
    2100015873, 2100015889, 2100016964, 2100017469, 2100017761, 2100017785, 2200011753, 2200011806, 2200013427, 2200013432,
    2200013707, 2200013712, 2200015155, 2200015455, 2200015872, 2200017856, 2200018112, 2300010821, 2300011759, 2300012256,
    2300013310, 2300013714, 2300015492, 2300016613, 2300016641, 2300017406, 2300017409, 2300017460, 2300017745, 2300017753,
    2300017808, 2300018124, 2300018216, 2300019005, 2300091602, 2300091605, 2300093006, 2300093007, 2300093008, 2400010608,
    2400010615, 2400010620, 2400010735, 2400010740, 2400010756, 2400010762, 2400010771, 2400010820, 2400010844, 2400010879,
    2400010955, 2400010982, 2400010985, 2400010992, 2400011010, 2400011015, 2400011024, 2400011033, 2400011044, 2400011047,
    2400011066, 2400011103, 2400011111, 2400011118, 2400011165, 2400011178, 2400011221, 2400011225, 2400011226, 2400011234,
    2400011245, 2400011256, 2400011308, 2400011337, 2400011347, 2400011402, 2400011409, 2400011410, 2400011416, 2400011417,
    2400011418, 2400011419, 2400011420, 2400011423, 2400011424, 2400011425, 2400011426, 2400011428, 2400011429, 2400011430,
    2400011431, 2400011432, 2400011433, 2400011435, 2400011437, 2400011440, 2400011441, 2400011444, 2400011446, 2400011450,
    2400011451, 2400011453, 2400011454, 2400011455, 2400011456, 2400011459, 2400011461, 2400011462, 2400011465, 2400011468,
    2400011470, 2400011473, 2400011474, 2400011477, 2400011483, 2400011484, 2400011486, 2400011489, 2400011490, 2400011491,
    2400011494, 2400011496, 2400011497, 2400011498, 2400011501, 2400011503, 2400011504, 2400011505, 2400011510, 2400011514,
    2400011516, 2400011524, 2400011545, 2400011546, 2400011559, 2400011611, 2400011705, 2400011707, 2400011708, 2400011709,
    2400011714, 2400011716, 2400011717, 2400011722, 2400011727, 2400011732, 2400011735, 2400011738, 2400011740, 2400011749,
    2400011753, 2400011754, 2400011759, 2400011762, 2400011766, 2400011768, 2400011769, 2400011770, 2400011772, 2400011777,
    2400011778, 2400011782, 2400011784, 2400011785, 2400011787, 2400011788, 2400011789, 2400011794, 2400011795, 2400011806,
    2400011811, 2400011813, 2400011851, 2400011852, 2400011855, 2400011858, 2400011862, 2400011876, 2400011880, 2400011884,
    2400012131, 2400012133, 2400012139, 2400012151, 2400012257, 2400012260, 2400012261, 2400012262, 2400012280, 2400012282,
    2400012414, 2400012417, 2400012424, 2400012433, 2400012443, 2400012557, 2400012560, 2400012601, 2400012605, 2400012619,
    2400013254, 2400013260, 2400013262, 2400013305, 2400013310, 2400013331, 2400013403, 2400013411, 2400013418, 2400013420,
    2400013424, 2400013510, 2400013761, 2400015416, 2400015804, 2400015830, 2400015896, 2400016607, 2400016617, 2400016635,
    2400016640, 2400016642, 2400016644, 2400017431, 2400017712, 2400091007, 2400093016, 2410306105, 2200016815, 2300012657,
    2300016915, 2300017439, 2400010629, 2400010981, 2400011016, 2400011020, 2400011025, 2400011046, 2400011049, 2400011112,
    2400011114, 2400011157, 2400011176, 2400011182, 2400011205, 2400011220, 2400011229, 2400011411, 2400011413, 2400011445,
    2400011447, 2400011457, 2400011466, 2400011492, 2400011507, 2400011574, 2400011721, 2400011737, 2400011878, 2400012110,
    2400012143, 2400012149, 2400012403, 2400012554, 2400013320, 2400013414, 2400015881, 2400016620, 2400017745, 2400017773,
    2400017852, 2410120125, 2100017405, 2300013411, 2300017766, 2300017770, 2400010622, 2400010759, 2400010951, 2400010952,
    2400010967, 2400011005, 2400011009, 2400011014, 2400011018, 2400011026, 2400011031, 2400011036, 2400011062, 2400011107,
    2400011125, 2400011128, 2400011158, 2400011168, 2400011171, 2400011203, 2400011214, 2400011237, 2400011241, 2400011248,
    2400011258, 2400011340, 2400011481, 2400011533, 2400011713, 2400011763, 2400011771, 2400011868, 2400012113, 2400012124,
    2400012154, 2400012266, 2400012402, 2400012421, 2400012425, 2400012618, 2400013405, 2400013417, 2400013422, 2400013774,
    2400015853, 2400015888, 2400016627, 2400016634, 2400017729, 2400018908, 2400019409, 2400090102, 2400092704, 2300014219,
    2400010621, 2400010973, 2400010974, 2400010988, 2400010989, 2400010998, 2400011028, 2400011050, 2400011060, 2400011131,
    2400011162, 2400011172, 2400011185, 2400011186, 2400011239, 2400011499, 2400011509, 2400012405, 2400012561, 2400012562,
    2400012609, 2400012659, 2400013426, 2400013765, 2400015832, 2400015840, 2400015844, 2400015857, 2400015863, 2400015873,
    2400016606, 2400016624, 2400016638, 2400016647, 2400016661, 2400017772, 2400010964, 2400010975, 2400010996, 2400011001,
    2400011011, 2400011041, 2400011059, 2400011064, 2400011210, 2400011257, 2400011260, 2400012120, 2400012148, 2400012304,
    2400012434, 2400012508, 2400012510, 2400012511, 2400013275, 2400013322, 2400013404, 2400013406, 2400013408, 2400013763,
    2400017474, 2400017706, 2400018708


}

print(len(sent_id))

res1 = []
res2 = []
for i in student_id:
    if i in sent_id:
        continue

    res2.append(i)
    if i < 2e9:
        res1.append(f"{i}@pku.edu.cn")
    else:
        res1.append(f"{i}@stu.pku.edu.cn")

print(','.join(res1))
print(', '.join(map(str, res2)))

'''
我是mac机器，可以这样发送，但是北大邮箱总把收到的邮件归到Spam里面。
(cat mail.txt; uuencode 20230820-Wechat.jpg 20230820-Wechat.jpg)|mail -s "202308 计算概论（B）（12班）课程微信群" x@pku.edu.cn

所以我现在是程序输出要发送同学的邮箱地址列表，拷贝下来，在浏览器邮件里面发送。
'''
