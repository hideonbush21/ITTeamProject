import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    qs_rank1 = [
        {'title': 'learn more from here',
         'url': 'https://www.mit.edu/',
         'views': 21,
         'content': "Massachusetts Institute of Technology (MIT) is a private land-grant research university in Cambridge, Massachusetts. Established in 1861, MIT has since played a key role (MIT150) in the development of modern technology and science, ranking it among the most prestigious academic institutions in the world.Founded in response to the increasing industrialization of the United States, MIT adopted a European polytechnic university model and stressed laboratory instruction in applied science and engineering. The institute has an urban campus that extends more than a mile (1.6 km) alongside the Charles River, and encompasses a number of major off-campus facilities such as the MIT Lincoln Laboratory, the Bates Center, and the Haystack Observatory, as well as affiliated laboratories such as the Broad and Whitehead Institutes.",
         'rank': 1},
        # {'title': 'How to Think like a Computer Scientist',
        #  'url': 'http://www.greenteapress.com/thinkpython/',
        #  'views': 19,
        #  'content': 'UCL',
        #  'rank': 2},
        # {'title': 'Learn Python in 10 Minutes',
        #  'url': 'http://www.korokithakis.net/tutorials/python/',
        #  'views': 32,
        #  'content': 'UoG',
        #  'rank': 3}]
    ]
    qs_rank2 = [
        {'title': 'learn more from here',
         'url': 'https://www.ox.ac.uk/',
         'views': 48,
         'content': "The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation. It grew rapidly from 1167 when Henry II banned English students from attending the University of Paris. After disputes between students and Oxford townsfolk in 1209, some academics fled north-east to Cambridge where they established what became the University of Cambridge. The two English ancient universities share many common features and are jointly referred to as Oxbridge.",
         'rank': 2},
    ]
    qs_rank3 = [
        {'title': 'learn more from here',
         'url': 'https://www.stanford.edu/',
         'views': 98,
         'content': "Stanford University, officially Leland Stanford Junior University,is a private research university in Stanford, California. The campus occupies 8,180 acres, among the largest in the United States, and enrolls over 17,000 students. Stanford is ranked among the best universities in the world by academic publications.Stanford was founded in 1885 by Leland and Jane Stanford in memory of their only child, Leland Stanford Jr., who had died of typhoid fever at age 15 the previous year. Leland Stanford was a U.S. senator and former governor of California who made his fortune as a railroad tycoon. The school admitted its first students on October 1, 1891, as a coeducational and non-denominational institution. Stanford University struggled financially after the death of Leland Stanford in 1893 and again after much of the campus was damaged by the 1906 San Francisco earthquake. Following World War II, provost Frederick Terman supported faculty and graduates' entrepreneurialism to build self-sufficient local industry in what would later be known as Silicon Valley.",
         'rank': 3},
    ]
    qs_rank4 = [
        {'title': 'learn more from here',
         'url': 'https://www.cam.ac.uk/',
         'views': 1022,
         'content': "The University of Cambridge is a collegiate research university in Cambridge, United Kingdom. Founded in 1209 and granted a royal charter by Henry III in 1231, Cambridge is the second-oldest university in the English-speaking world and the world's fourth-oldest surviving university. The university grew out of an association of scholars who left the University of Oxford after a dispute with the townspeople. The two English ancient universities share many common features and are often jointly referred to as Oxbridge.",
         'rank': 3},
    ]
    qs_rank5 = [
        {'title': 'learn more from here',
         'url': 'https://www.harvard.edu//',
         'views': 826,
         'content': "Harvard University is a private Ivy League research university in Cambridge, Massachusetts. Established in 1636 and named for its first benefactor, clergyman John Harvard, Harvard is the oldest institution of higher learning in the United States and among the most prestigious in the world.The Massachusetts colonial legislature, the General Court, authorized Harvard's founding. In its early years, Harvard College primarily trained Congregational and Unitarian clergy, although it has never been formally affiliated with any denomination. Its curriculum and student body were gradually secularized during the 18th century, and by the 19th century, Harvard had emerged as the central cultural establishment among the Boston elite. Following the American Civil War, President Charles William Eliot's long tenure (1869–1909) transformed the college and affiliated professional schools into a modern research university; Harvard became a founding member of the Association of American Universities in 1900. James B. Conant led the university through the Great Depression and World War II; he liberalized admissions after the war.",
         'rank': 5},
    ]
    qs_rank6 = [
        {'title': 'learn more from here',
         'url': 'https://www.caltech.edu//',
         'views': 23,
         'content': "The California Institute of Technology (Caltech) is a private research university in Pasadena, California. The university is known for its strength in science and engineering, and is one among a small group of institutes of technology in the United States which is primarily devoted to the instruction of pure and applied sciences.Caltech was founded as a preparatory and vocational school by Amos G. Throop in 1891 and began attracting influential scientists such as George Ellery Hale, Arthur Amos Noyes, and Robert Andrews Millikan in the early 20th century. The vocational and preparatory schools were disbanded and spun off in 1910 and the college assumed its present name in 1920. In 1934, Caltech was elected to the Association of American Universities, and the antecedents of NASA's Jet Propulsion Laboratory, which Caltech continues to manage and operate, were established between 1936 and 1943 under Theodore von Kármán.",
         'rank': 6},
    ]
    qs_rank7 = [
        {'title': 'learn more from here',
         'url': 'https://www.imperial.ac.uk//',
         'views': 3146,
         'content': "Imperial College London (legally Imperial College of Science, Technology and Medicine) is a public research university in London. Imperial grew out of Prince Albert's vision of an area for culture, including the Royal Albert Hall, Imperial Institute, numerous museums, and the Royal Colleges that would go on to form the college. In 1907, Imperial College was established by Royal Charter, merging the Royal College of Science, Royal School of Mines, and City and Guilds College. In 1988, the Imperial College School of Medicine was formed by combining with St Mary's Hospital Medical School. In 2004, Queen Elizabeth II opened the Imperial College Business School.",
         'rank': 7},
    ]
    qs_rank8 = [
        {'title': 'learn more from here',
         'url': 'https://ethz.ch/en.html',
         'views': 221,
         'content': "ETH Zürich (English: ETH; Swiss Federal Institute of Technology in Zürich; German: Eidgenössische Technische Hochschule Zürich) is a public research university in the city of Zürich, Switzerland. Founded by the Swiss Federal Government in 1854 with the stated mission to educate engineers and scientists, the school focuses exclusively on science, technology, engineering, and mathematics. Like its sister institution EPFL, it is part of the Swiss Federal Institutes of Technology Domain, part of the Swiss Federal Department of Economic Affairs, Education and Research.",
         'rank': 8},
    ]
    qs_rank9 = [
        {'title': 'learn more from here',
         'url': 'https://www.ucl.ac.uk//',
         'views': 231,
         'content': "University College London, which operates as UCL, is a major public research university located in London, United Kingdom. UCL is ranked amongst the world's best universities by various academic publications. UCL is a member institution of the federal University of London, and is the second-largest university in the United Kingdom by total enrolment, after the Open University, and the largest by postgraduate enrolment.",
         'rank': 8},
    ]
    qs_rank10 = [
        {'title': 'learn more from here',
         'url': 'https://www.uchicago.edu/',
         'views': 21,
         'content': "The University of Chicago (UChicago, U of C, or Chicago) is a private research university in Chicago, Illinois. Founded in 1890, its main campus is located in Chicago's Hyde Park neighborhood. It enrolled 16,445 students in Fall 2019, including 6,286 undergraduates and 10,159 graduate students. The University of Chicago is ranked among the best universities in the world by major education publications, and it is among the most selective in the United States.",
         'rank': 10},
    ]
    qs_rank11 = [
        {'title': 'learn more from here',
         'url': 'https://nus.edu.sg/',
         'views': 212,
         'content': "The National University of Singapore (NUS) is a national research university based in Singapore. Founded in 1905 as the Straits Settlements and Federated Malay States Government Medical School, NUS is the oldest higher education institution in Singapore. According to most rankings, it is considered to be one of the best universities in the Asia-Pacific and is among the top 40 universities in the world. NUS is a comprehensive research university, offering degree programmes in a wide range of disciplines at both the undergraduate and postgraduate levels, including in the sciences, medicine and dentistry, design and environment, law, arts and social sciences, engineering, business, computing, and music.",
         'rank': 11},
        # {'title': 'How to Think like a Computer Scientist',
        #  'url': 'http://www.greenteapress.com/thinkpython/',
        #  'views': 19,
        #  'content': 'UCL',
        #  'rank': 2},
        # {'title': 'Learn Python in 10 Minutes',
        #  'url': 'http://www.korokithakis.net/tutorials/python/',
        #  'views': 32,
        #  'content': 'UoG',
        #  'rank': 3}]
    ]

    qs_rank12 = [
        {'title': 'learn more from here',
         'url': 'https://www.ntu.edu.sg//',
         'views': 456,
         'content': "The Nanyang Technological University, Singapore (NTU), is the second oldest public autonomous research university in Singapore and is considered to be one of the top universities in the world. NTU is consistently ranked within the top 100 universities in the world according to most rankings, and has been ranked as overall 1st in the ranking of young universities in the QS World University Rankings since 2015 as of April 2021 It has 23,951 full-time enrolled students and 3846 full-time teaching staff; it has achieved 12th in the overall ranking of current QS World University Rankings as of June 2021.",
         'rank': 12},
    ]
    qs_rank13 = [
        {'title': 'learn more from here',
         'url': 'https://www.upenn.edu//',
         'views': 956,
         'content': "The University of Pennsylvania (Penn or UPenn) is a private Ivy League research university in Philadelphia, Pennsylvania. The university, established as the College of Philadelphia, claims a founding date of 1740 and is one of the nine colonial colleges chartered prior to the U.S. Declaration of Independence. Benjamin Franklin, Penn's founder and first president, advocated an educational program that trained leaders in commerce, government, and public service, similar to a modern liberal arts curriculum with a practical perspective.",
         'rank': 13},
    ]
    qs_rank14 = [
        {'title': 'learn more from here',
         'url': 'https://www.epfl.ch/en//',
         'views': 423,
         'content': "The École polytechnique fédérale de Lausanne (EPFL) is a public research university located in Lausanne, Switzerland. It specializes in natural sciences and engineering. It is one of the two Swiss Federal Institutes of Technology, with three main missions: education, research and technology transfer. The QS World University Rankings ranked EPFL as the 14th best university in the world across all fields in 2021, whereas THE World University Rankings ranked EPFL as the world's 19th best school for engineering and technology in 2020.",
         'rank': 14},
    ]
    qs_rank15 = [
        {'title': 'learn more from here',
         'url': 'https://www.yale.edu/',
         'views': 371,
         'content': "Yale University is a private Ivy League research university in New Haven, Connecticut. Founded in 1701 as the Collegiate School, it is the third-oldest institution of higher education in the United States and one of the nine Colonial Colleges chartered before the American Revolution. The Collegiate School was renamed Yale College in 1718 to honor the school's largest private benefactor for the first century of its existence, Elihu Yale. Yale University is referred to as a member of the Big Three (colleges), is consistently ranked as one of the top universities and is considered one of the most prestigious in the nation and in the world",
         'rank': 14},
    ]
    qs_rank16 = [
        {'title': 'learn more from here',
         'url': 'https://www.ed.ac.uk//',
         'views': 9988,
         'content': "The University of Edinburgh (Scottish Gaelic: Oilthigh Dhùn Èideann; abbreviated as Edin. in post-nominals) is a public research university in Edinburgh, Scotland. Granted a royal charter signed by James VI in 1582 and officially opened in 1583, it is one of Scotland's four ancient universities, and the sixth-oldest existing university in the English-speaking world. The university has five main campuses in the city of Edinburgh, which include many buildings of historical and architectural significance such as those in the Old Town. The university played an important role in Edinburgh becoming a chief intellectual centre during the Scottish Enlightenment, contributing to the city being nicknamed the Athens of the North.",
         'rank': 16},
    ]
    qs_rank17 = [
        {'title': 'learn more from here',
         'url': 'https://www.tsinghua.edu.cn/en/index.htm',
         'views': 8888,
         'content': "Tsinghua University (Chinese: 清华大学) is a major public research university in Beijing, and a member of the C9 League of Chinese universities. Since its establishment in 1911, it has produced many notable leaders in science, engineering, politics, business, academia, and culture. The university is ranked as the 15th best university in the world in the QS World University Rankings, and is ranked No.1 in Asia by the THE Asia University Rankings and the U.S. News and World Report.",
         'rank': 17},
    ]
    qs_rank18 = [
        {'title': 'learn more from here',
         'url': 'https://www.pku.edu.cn/',
         'views': 7777,
         'content': "Peking University (Chinese: 北京大学, informally Beida 北大, PKU; lit. 'Beijing University'), is a major research university in Beijing, China, and a member of the elite C9 League of Chinese universities. Peking University was established as the Imperial University of Peking in 1898 when it received its first royal charter by the Guangxu Emperor. A successor of the older Guozijian Imperial College, the university's romanized name 'Peking' retains the older transliteration of 'Beijing' that has been superseded in most other contexts. Perennially ranked as one of the top academic institutions in China and the world, as of 2021, it is ranked 18th globally by QS Ranking, and 2nd in the Asia-Pacific and emerging countries by Times Higher Education.",
         'rank': 18},
    ]
    qs_rank19 = [
        {'title': 'learn more from here',
         'url': 'https://www.columbia.edu/',
         'views': 5,
         'content': "Columbia University (also known as Columbia, and officially as Columbia University in the City of New York) is a private Ivy League research university in New York City. Established in 1754 as King's College on the grounds of Trinity Church in Manhattan, Columbia is the oldest institution of higher education in New York and the fifth-oldest institution of higher learning in the United States. It is one of nine colonial colleges founded prior to the Declaration of Independence, seven of which belong to the Ivy League. Columbia is ranked among the top universities in the world by major education publications.",
         'rank': 19},
    ]
    qs_rank20 = [
        {'title': 'learn more from here',
         'url': 'https://www.princeton.edu/',
         'views': 13,
         'content': "Princeton University is a private Ivy League research university in Princeton, New Jersey. Founded in 1746 in Elizabeth as the College of New Jersey, Princeton is the fourth-oldest institution of higher education in the United States and one of the nine colonial colleges chartered before the American Revolution. The institution moved to Newark in 1747, and then to the current site nine years later. It officially became a university in 1896 and was subsequently renamed Princeton University.",
         'rank': 20},
    ]
    qs_rank21 = [
        {'title': 'learn more from here',
         'url': 'https://www.cornell.edu/',
         'views': 76,
         'content': "Cornell University  is a private Ivy League statutory land-grant research university in Ithaca, New York. Founded in 1865 by Ezra Cornell and Andrew Dickson White, it has consistently been ranked among the top universities in the world by major educational publications.Cornell was founded with the intention to teach and make contributions in all fields of knowledge—from the classics to the sciences, and from the theoretical to the applied. These ideals, unconventional for the time, are captured in Cornell's founding principle, a popular 1868 quotation from founder Ezra Cornell: ""I would found an institution where any person can find instruction in any study.""The university is broadly organized into seven undergraduate colleges and seven graduate divisions at its main Ithaca campus, with each college and division defining its specific admission standards and academic programs in near autonomy. The university also administers two satellite medical campuses, one in New York City and one in Education City, Qatar.",
         'rank': 21},
    ]
    qs_rank22 = [
        {'title': 'learn more from here',
         'url': 'https://www.hku.hk/',
         'views': 3,
         'content': "The University of Hong Kong (abbreviated as HKU) is a public research university in Hong Kong. Founded in 1911, its origins trace back to the Hong Kong College of Medicine for Chinese, which was founded in 1887. It is the oldest tertiary institution in Hong Kong. HKU was also the first university established by the British in East Asia.As of 2020, HKU ranks third in Asia and 22nd internationally by QS, and fourth in Asia and 35th internationally by THE. It has been commonly regarded as one of the most internationalized universities in the world as well as one of the most prestigious universities in Asia. Today, HKU has ten academic faculties with English as the main language of instruction. HKU also ranks highly in the sciences, dentistry, biomedicine, architecture,  education, humanities, law, economics, business administration, linguistics, political science, and the social work and social administration.",
         'rank': 22},
    ]
    qs_rank23 = [
        {'title': 'learn more from here',
         'url': 'https://www.u-tokyo.ac.jp/ja/index.html',
         'views': 673,
         'content': "The University of Tokyo (東京大学, Tōkyō daigaku), abbreviated as Todai (東大, Tōdai) or UTokyo, is a public research university located in Bunkyō, Tokyo, Japan. Established in 1877, the university is the first imperial university and currently selected as a Top Type university of Top Global University Project by the Japanese government.",
         'rank': 23},
    ]
    qs_rank24 = [
        {'title': 'learn more from here',
         'url': 'https://umich.edu/',
         'views': 99,
         'content': "The University of Michigan (UM, U-M, U of M, UMich, or Michigan) is a public research university in Ann Arbor, Michigan. Founded in 1817 in Detroit, as the Catholepistemiad, or the University of Michigania, 20 years before the territory became a state, the university is Michigan's oldest. The school was moved to Ann Arbor in 1837 onto 40 acres (16 ha) of what is now known as Central Campus. Since its establishment in Ann Arbor, the flagship university campus has expanded to include more than 584 major buildings with a combined area of more than 780 acres (3.2 km2) spread out over Central Campus and North Campus, two satellite campuses in Flint and Dearborn, and a Center in Detroit. The university is a founding member of the Association of American Universities.",
         'rank': 23},
    ]
    qs_rank25 = [
        {'title': 'learn more from here',
         'url': 'https://www.jhu.edu/',
         'views': 55,
         'content': "The Johns Hopkins University (Johns Hopkins, Hopkins, or JHU) is a private research university in Baltimore, Maryland. Founded in 1876, the university was named for its first benefactor, the American entrepreneur and philanthropist Johns Hopkins.Johns Hopkins is considered the first research university in the United States. Hopkins's $7 million bequest to establish the university was the largest philanthropic gift in the history of the United States up to that time. Daniel Coit Gilman, who was inaugurated as Johns Hopkins' first president on February 22, 1876, led the university to revolutionize higher education in the U.S. by integrating teaching and research. In 1900, Johns Hopkins became a founding member of the American Association of Universities. The university has since led all U.S. universities in annual research expenditures.",
         'rank': 25},
    ]
    qs_rank26 = [
        {'title': 'learn more from here',
         'url': 'https://www.utoronto.ca/',
         'views': 645,
         'content': "The University of Toronto (U of T or UToronto) is a public research university in Toronto, Ontario, Canada, located on the grounds that surround Queen's Park. It was founded by royal charter in 1827 as King's College, the first institution of higher learning in Upper Canada. Originally controlled by the Church of England, the university assumed its present name in 1850 upon becoming a secular institution. As a collegiate university, it comprises eleven colleges each with substantial autonomy on financial and institutional affairs and significant differences in character and history. The university also operates two suburban campuses located in Scarborough and Mississauga.",
         'rank': 26},
    ]
    qs_rank27 = [
        {'title': 'learn more from here',
         'url': 'https://www.mcgill.ca/',
         'views': 31,
         'content': "",
         'rank': 27},
    ]
    qs_rank28 = [
        {'title': 'learn more from here',
         'url': 'https://www.anu.edu.au/',
         'views': 85,
         'content': "The Australian National University (ANU) is a public research university located in Canberra, the capital of Australia. Its main campus in Acton encompasses seven teaching and research colleges, in addition to several national academies and institutes.ANU is regarded as one of the world's leading research universities, and is ranked as the number one university in Australia and the Southern Hemisphere by the 2022 QS World University Rankings. It is ranked 27th in the world by the 2022 QS World University Rankings, and 59th in the world (third in Australia) by the 2021 Times Higher Education.",
         'rank': 27},
    ]
    qs_rank29 = [
        {'title': 'learn more from here',
         'url': 'https://www.manchester.ac.uk/',
         'views': 333,
         'content': "The University of Manchester is a public research university in Manchester, England. The main campus is south of Manchester City Centre on Oxford Road. The university owns and operates major cultural assets such as the Manchester Museum, Whitworth Art Gallery, John Rylands Library and Jodrell Bank Observatory—a UNESCO World Heritage Site.",
         'rank': 27},
    ]
    qs_rank30 = [
        {'title': 'learn more from here',
         'url': 'https://www.northwestern.edu/',
         'views': 90,
         'content': "Northwestern University is a private research university in Evanston, Illinois. Founded in 1851, Northwestern is the oldest chartered university in Illinois and is ranked among the most prestigious academic institutions in the world.Chartered by the Illinois General Assembly in 1851, Northwestern was established to serve the former Northwest Territory. The university was initially affiliated with the Methodist Episcopal Church, but soon grew to be non-sectarian. In 1882, Northwestern became a founding member of the Big Ten Conference, and later joined the Association of American Universities as an early member in 1917. The university was the third largest university in the United States by the 1900s under Henry Wade Rogers.",
                    'rank': 30},
    ]

    qs_rank31 = [
        {'title': 'learn more from here',
         'url': 'https://www.fudan.edu.cn/',
         'views': 555,
         'content': "Fudan University (simplified Chinese: 复旦大学; traditional Chinese: 復旦大學; pinyin: Fùdàn Dàxué) is a major public research university in Shanghai, China. It is widely considered one of the most prestigious and selective universities in China. Founded in 1905, shortly before the end of China's imperial Qing dynasty, Fudan was the first university established independently by the Chinese people. Fudan is a member of the elite C9 League and a Chinese Ministry of Education Class A Double First Class University.",
         'rank': 31},
    ]
    qs_rank32 = [
        {'title': 'learn more from here',
         'url': 'https://www.berkeley.edu/',
         'views': 97,
         'content': "The University of California, Berkeley (UC Berkeley, Berkeley, Cal, or California)[8][9] is a public land-grant research university in Berkeley, California. Established in 1868 as the University of California, it is the state's first land-grant university and the first campus of the University of California system. Its fourteen colleges and schools offer over 350 degree programs and enroll some 31,000 undergraduate and 12,000 graduate students.[3][10][11] Berkeley is ranked among the world's top universities by major educational publications.[12]",
         'rank': 32},
    ]
    qs_rank33 = [
        {'title': 'learn more from here',
         'url': 'https://www.kyoto-u.ac.jp/zh-cn',
         'views': 38,
         'content': "Kyoto University (京都大学, Kyōto daigaku), or KyotoU (京大, Kyōdai), is a public research university located in Kyoto, Japan. Founded in 1897, it is the second oldest university in Japan, one of the former Imperial Universities, the first three Designated National University and selected as a Top Type university of Top Global University Project by the Japanese government.[5] KyotoU is usually ranked amongst the top two in Japan, the top ten in Asia, and the world's top thirty institutions of higher education.",
         'rank': 33},
    ]
    qs_rank34 = [
        {'title': 'learn more from here',
         'url': 'https://hkust.edu.hk/',
         'views': 32,
         'content': "The Hong Kong University of Science and Technology (abbreviated as HKUST) is a public research university in Clear Water Bay Peninsula, Hong Kong. Founded in 1991 by the British Hong Kong Government, it was the territory's third institution to be granted university status.HKUST is commonly regarded as one of the fastest growing universities in the world. In 2019, the university was ranked seventh in Asia by QS and third by The Times, and around top 40 internationally. It was ranked 27th in the world and second in Hong Kong by QS 2021. It also ranked first in Times Higher Education Young University Rankings in 2019 and second by QS world's under-50 universities in 2020.",
         'rank': 34},
    ]
    qs_rank35 = [
        {'title': 'learn more from here',
         'url': 'https://www.kcl.ac.uk/',
         'views': 878,
         'content': "King's College London (informally King's or KCL) is a public research university located in London, United Kingdom, and a founding college and member institution of the federal University of London. King's was established in 1829 by King George IV and Arthur Wellesley, 1st Duke of Wellington, when it received its first royal charter (as a university college), and is one of the oldest universities in England. In 1836, King's became one of the two founding colleges of the University of London.",
         'rank': 35},
    ]
    qs_rank36 = [
        {'title': 'learn more from here',
         'url': 'https://en.snu.ac.kr/',
         'views': 332,
         'content': "Seoul National University (SNU; Korean: 서울대학교; Hanja: 서울大學校; RR: Seoul Daehakgyo, colloquially Seouldae) is a national research university located in Seoul, South Korea. It is one of the flagship Korean national universities.Founded in 1946, Seoul National University is considered to be the most prestigious university in the country. The university has three campuses: the main campus in Gwanak-gu and two additional campuses in Daehangno and Pyeongchang. The university comprises sixteen colleges, one graduate school and nine professional schools. The student body consists of nearly 17,000 undergraduate and 11,000 graduate students. According to data compiled by KEDI, the university spends more on its students per capita than any other universities in the country that enroll at least 10,000 students.",
         'rank': 36},
    ]
    qs_rank37 = [
        {'title': 'learn more from here',
         'url': 'https://www.unimelb.edu.au/',
         'views': 82,
         'content': "The University of Melbourne is a public research university located in Melbourne, Australia. Founded in 1853, it is Australia's second oldest university and the oldest in Victoria. Its main campus is located in Parkville, an inner suburb north of Melbourne's central business district, with several other campuses located across Victoria. Incorporated in the 19th century by the colony of Victoria, the University of Melbourne is one of Australia's six sandstone universities and a member of the Group of Eight, Universitas 21, Washington University's McDonnell International Scholars Academy, and the Association of Pacific Rim Universities. Since 1872 various residential colleges have become affiliated with the university, offering accommodation for students and faculty, and academic, sporting and cultural programs. There are ten colleges located on the main campus and in nearby suburbs.",
         'rank': 37},
    ]
    qs_rank38 = [
        {'title': 'learn more from here',
         'url': 'https://www.sydney.edu.au/',
         'views': 92,
         'content': "The University of Sydney (USYD, or informally Sydney Uni) is a public research university located in Sydney, Australia. Founded in 1850, it is Australia's first university and is regarded as one of the world's leading universities. The university is known as one of Australia's six sandstone universities. Its campus, spreading across the inner-city suburbs of Camperdown and Darlington, is ranked in the top 10 of the world's most beautiful universities by the British Daily Telegraph and the American Huffington Post. The university comprises eight academic faculties and university schools, through which it offers bachelor, master and doctoral degrees.",
         'rank': 38},
    ]
    qs_rank39 = [
        {'title': 'learn more from here',
         'url': 'https://www.cuhk.edu.hk/chinese/index.html',
         'views': 23,
         'content': "The Chinese University of Hong Kong (abbreviated CUHK) is a public research university in Shatin, Hong Kong, formally established in 1963 by a charter granted by the Legislative Council of Hong Kong. It is the territory's second-oldest university and was founded as a federation of three existing colleges – Chung Chi College, New Asia College and United College – the oldest of which was founded in 1949.",
         'rank': 39},
    ]
    qs_rank40 = [
        {'title': 'learn more from here',
         'url': 'https://www.ucla.edu/',
         'views': 91,
         'content': "The University of California, Los Angeles (UCLA) is a public land-grant research university in Los Angeles, California. UCLA traces its early origins back to 1882 as the southern branch of the California State Normal School (now San Jose State University). It became the Southern Branch of the University of California in 1919, making it the second-oldest (after UC Berkeley) of the 10-campus University of California system.",
         'rank': 40},
    ]

    qs_rank41 = [
        {'title': 'learn more from here',
         'url': 'https://www.kaist.ac.kr/en/',
         'views': 3,
         'content': "KAIST (formally the Korea Advanced Institute of Science and Technology) is a national research university located in Daedeok Innopolis, Daejeon, South Korea. KAIST was established by the Korean government in 1971 as the nation's first public, research-oriented science and engineering institution. KAIST is considered to be one of the most prestigious universities in the nation. KAIST has been internationally accredited in business education, and hosting the Secretariat of AAPBS. KAIST has approximately 10,200 full-time students and 1,140 faculty researchers and had a total budget of US$765 million in 2013, of which US$459 million was from research contracts.",
         'rank': 41},
    ]
    qs_rank42 = [
        {'title': 'learn more from here',
         'url': 'https://www.nyu.edu/',
         'views': 30,
         'content': "New York University (NYU) is a private research university in New York City. Chartered in 1831 by the New York State Legislature, NYU was founded by a group of New Yorkers led by then Secretary of the Treasury Albert Gallatin. In 1832, the initial non-denominational all-male institution began its first classes near City Hall based on a curriculum focused on a secular education. The university, in 1833, then moved and has maintained its main campus in Greenwich Village surrounding Washington Square Park. Since then, the university has added an engineering school in Brooklyn's MetroTech Center and graduate schools throughout Manhattan. NYU has become the largest private university in the United States by enrollment, with a total of 51,848 enrolled students, including 26,733 undergraduate students and 25,115 graduate students, in 2019. NYU also receives the most applications of any private institution in the United States and admissions is considered highly selective.",
         'rank': 42},
    ]
    qs_rank43 = [
        {'title': 'learn more from here',
         'url': 'https://www.unsw.edu.au/',
         'views': 94,
         'content': "The University of New South Wales (UNSW; branded as UNSW Sydney) is a public research university based in Sydney, New South Wales, Australia. It is one of the founding members of Group of Eight, a coalition of Australian research-intensive universities.",
         'rank': 43},
    ]
    qs_rank44 = [
        {'title': 'learn more from here',
         'url': 'https://psl.eu/en',
         'views': 77,
         'content': "Paris Sciences et Lettres University (PSL University or simply PSL) is a public research university in Paris, France. It was established in 2010 and formally created as a university in 2019. It is a collegiate university with 11 constituent schools. PSL is located in central Paris, with its main sites in the Latin Quarter, at the Jourdan campus, at Porte Dauphine in northern Paris, and at Carré Richelieu.",
         'rank': 44},
    ]
    qs_rank45 = [
        {'title': 'learn more from here',
         'url': 'https://www.zju.edu.cn/english/',
         'views': 870,
         'content': "Zhejiang University (abbreviated ZJU; Chinese: 浙江大学; pinyin: Zhèjiāng Dàxué), also colloquially referred to as Zheda (浙大; Zhèdà), is a public research university, and a member of the elite C9 League. It is located in Hangzhou, the capital of Zhejiang Province. Founded in 1897, Zhejiang University is one of China's oldest, most selective, and most prestigious institutions of higher education. The university is organized into 37 colleges, schools, and departments offering more than 140 undergraduate and 300 graduate programs.",
         'rank': 45},
    ]
    qs_rank46 = [
        {'title': 'learn more from here',
         'url': 'https://www.ubc.ca/',
         'views': 43,
         'content': "The University of British Columbia (UBC) is a public research university with campuses in Vancouver and Kelowna, British Columbia. Established in 1908, UBC is British Columbia's oldest university. The university ranks among the top three universities in Canada. With an annual research budget of $600 million, UBC funds over 8,000 projects a year.",
         'rank': 46},
    ]
    qs_rank47 = [
        {'title': 'learn more from here',
         'url': 'https://www.uq.edu.au/',
         'views': 55,
         'content': "The University of Queensland (UQ, or Queensland University) is a public research university located primarily in Brisbane, the capital city of the Australian state of Queensland. Founded in 1909 by the Queensland parliament, UQ is one of the six sandstone universities, an informal designation of the oldest university in each state. The University of Queensland was ranked second nationally by the Australian Research Council in the latest research assessment and equal second in Australia based on the average of four major global university league tables. The University of Queensland is a founding member of edX, Australia's research-intensive Group of Eight and the global Universitas 21 network.",
         'rank': 47},
    ]
    qs_rank48 = [
        {'title': 'learn more from here',
         'url': 'https://ucsd.edu/',
         'views': 110,
         'content': "The University of California, San Diego (UC San Diego or, colloquially, UCSD[a]) is a public land-grant research university in San Diego, California. Established in 1960 near the pre-existing Scripps Institution of Oceanography, UC San Diego is the southernmost of the ten campuses of the University of California, and offers over 200 undergraduate and graduate degree programs, enrolling 31,842 undergraduate and 8,631 graduate students. The university occupies 2,178 acres (881 ha) near the coast of the Pacific Ocean, with the main campus resting on approximately 1,152 acres (466 ha). UC San Diego is ranked among the best universities in the world by major college and university rankings.",
         'rank': 48},
    ]
    qs_rank49 = [
        {'title': 'learn more from here',
         'url': 'https://www.lse.ac.uk/',
         'views': 551,
         'content': "The London School of Economics and Political Science (LSE or the LSE) is a public research university located in London, England, and a member institution of the federal University of London. Founded in 1895, by Fabian Society members Sidney Webb, Beatrice Webb, Graham Wallas, and George Bernard Shaw, LSE joined the University of London in 1900 and established its first degree courses under the auspices of the university in 1901.[7] LSE began awarding its degrees in its own name in 2008,[8] prior to which it awarded degrees of the University of London. The motto of the university is Rerum cognoscere causas which in Latin, means; To know the cause of things.",
         'rank': 49},
    ]
    qs_rank50 = [
        {'title': 'learn more from here',
         'url': 'https://en.sjtu.edu.cn/',
         'views': 323,
         'content': "Shanghai Jiao Tong University (SJTU; simplified Chinese: 上海交通大学; traditional Chinese: 上海交通大學) is a major research university in Shanghai. Established on April 8, 1896, as Nanyang Public School by an imperial edict issued by the Guangxu Emperor, it is one of China's oldest universities. Shanghai Jiao Tong University is a C9 League university and a Chinese Ministry of Education Class A Double First Class University.",
         'rank': 50},
    ]

    cats = {
        'Massachusetts Institute of Technology (MIT)': {'pages': qs_rank1, 'views': 128, 'likes': 64, 'rank': 1},
        'University of Oxford': {'pages': qs_rank2, 'views': 112, 'likes': 54, 'rank': 2},
        'Stanford University': {'pages': qs_rank3, 'views': 176, 'likes': 1124, 'rank': 3},
        'University of Cambridge': {'pages': qs_rank4, 'views': 454, 'likes': 767, 'rank': 4},
        'Harvard University': {'pages': qs_rank5, 'views': 123, 'likes': 989, 'rank': 5},
        'California Institute of Technology (Caltech)': {'pages': qs_rank6, 'views': 565, 'likes': 988, 'rank': 6},
        'Imperial College London': {'pages': qs_rank7, 'views': 1281, 'likes': 646, 'rank': 7},
        'ETH Zurich - Swiss Federal Institute of Technology': {'pages': qs_rank8, 'views': 756, 'likes': 5117, 'rank': 8},
        'UCL': {'pages': qs_rank9, 'views': 777, 'likes': 4396, 'rank': 9},
        'University of Chicago': {'pages': qs_rank10, 'views': 655, 'likes': 641, 'rank': 10},

        'National University of Singapore (NUS)': {'pages': qs_rank11, 'views': 655, 'likes': 641, 'rank': 11},
        'Nanyang Technological University, Singapore (NTU)': {'pages': qs_rank12, 'views': 141, 'likes': 1641, 'rank': 12},
        'University of Pennsylvania': {'pages': qs_rank13, 'views': 141, 'likes': 1641, 'rank': 13},
        'EPFL': {'pages': qs_rank14, 'views': 141, 'likes': 1641, 'rank': 14},
        'Yale University': {'pages': qs_rank15, 'views': 141, 'likes': 1641, 'rank': 15},
        'The University of Edinburgh': {'pages': qs_rank16, 'views': 141, 'likes': 1641, 'rank': 16},
        'Tsinghua University': {'pages': qs_rank17, 'views': 141, 'likes': 1641, 'rank': 17},
        'Peking University': {'pages': qs_rank18, 'views': 141, 'likes': 1641, 'rank': 18},
        'Columbia University': {'pages': qs_rank19, 'views': 141, 'likes': 1641, 'rank': 19},
        'Princeton University': {'pages': qs_rank20, 'views': 141, 'likes': 1641, 'rank': 20},
        'Cornell University': {'pages': qs_rank21, 'views': 141, 'likes': 1641, 'rank': 21},
        'The University of Hong Kong': {'pages': qs_rank22, 'views': 141, 'likes': 1641, 'rank': 22},
        'The University of Tokyo': {'pages': qs_rank23, 'views': 141, 'likes': 1641, 'rank': 23},
        'University of Michigan-Ann Arbor': {'pages': qs_rank24, 'views': 141, 'likes': 1641, 'rank': 24},
        'Johns Hopkins University': {'pages': qs_rank25, 'views': 141, 'likes': 1641, 'rank': 25},
        'University of Toronto': {'pages': qs_rank26, 'views': 141, 'likes': 1641, 'rank': 26},
        'McGill University': {'pages': qs_rank27, 'views': 141, 'likes': 1641, 'rank': 27},
        'The Australian National University': {'pages': qs_rank28, 'views': 141, 'likes': 1641, 'rank': 28},
        'The University of Manchester': {'pages': qs_rank29, 'views': 141, 'likes': 1641, 'rank': 29},
        'Northwestern University': {'pages': qs_rank30, 'views': 141, 'likes': 1641, 'rank': 30},
        'Fudan University': {'pages': qs_rank31, 'views': 141, 'likes': 1641, 'rank': 31},
        'University of California,Berkeley(UCB)': {'pages': qs_rank32, 'views': 141, 'likes': 1641, 'rank': 32},
        'Kyoto University': {'pages': qs_rank33, 'views': 141, 'likes': 1641, 'rank': 33},
        'The Hong Kong University of Science and Technology': {'pages': qs_rank34, 'views': 141, 'likes': 1641, 'rank': 34},
        'Kings College London': {'pages': qs_rank35, 'views': 141, 'likes': 1641, 'rank': 35},
        'Seoul National University': {'pages': qs_rank36, 'views': 141, 'likes': 1641, 'rank': 36},
        'The University of Melbourne': {'pages': qs_rank37, 'views': 141, 'likes': 1641, 'rank': 37},
        'The University of Sydney': {'pages': qs_rank38, 'views': 141, 'likes': 1641, 'rank': 38},
        'The Chinese University of Hong Kong (CUHK)': {'pages': qs_rank39, 'views': 141, 'likes': 1641, 'rank': 39},
        'University of California, Los Angeles (UCLA)': {'pages': qs_rank40, 'views': 141, 'likes': 1641, 'rank': 40},
        'KAIST - Korea Advanced Institute of Science & Technology': {'pages': qs_rank41, 'views': 141, 'likes': 1641, 'rank': 41},
        'New York University (NYU)': {'pages': qs_rank42, 'views': 141, 'likes': 1641, 'rank': 42},
        'The University of New South Wales (UNSW Sydney)': {'pages': qs_rank43, 'views': 141, 'likes': 1641, 'rank': 43},
        'Université PSL': {'pages': qs_rank44, 'views': 141, 'likes': 1641, 'rank': 44},
        'Zhejiang University': {'pages': qs_rank45, 'views': 141, 'likes': 1641, 'rank': 45},
        'University of British Columbia': {'pages': qs_rank46, 'views': 141, 'likes': 1641, 'rank': 46},
        'The University of Queensland': {'pages': qs_rank47, 'views': 141, 'likes': 1641, 'rank': 47},
        'University of California, San Diego (UCSD)': {'pages': qs_rank48, 'views': 141, 'likes': 1641, 'rank': 48},
        'The London School of Economics and Political Science (LSE)': {'pages': qs_rank49, 'views': 141, 'likes': 1641, 'rank': 49},
        'Shanghai Jiao Tong University': {'pages': qs_rank50, 'views': 141, 'likes': 1641, 'rank': 50},
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'], rank=cat_data['rank'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], content=p['content'], rank=p['rank'], views=p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, content='', rank=0, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.content = content
    p.rank = rank
    p.save()
    return p


def add_cat(name, views=0, likes=0, rank=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.rank = rank
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
