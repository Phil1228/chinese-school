#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate multilingual pages (en/fr/hi/id) for the Chinese school site."""
import os, html, json

ROOT = "/Users/Phil/Documents/git/chinese-school"
DOMAIN = "https://Yu.loong.click"
BRAND = "華語學堂"
BRAND_EN = "Mandarin School"

# WhatsApp / email (same on all)
WA = "https://wa.me/phil.deng"
WA_ID = "phil.deng"
EMAIL = "phoenixdkd@gmail.com"
MAILTO = "mailto:phoenixdkd@gmail.com"

# ---- per-language meta ----
LANGS = {
    "zh": {"name": "中文", "dir": "", "html_lang": "zh-HK",
           "nav": ["主頁","關於我們","課程列表","老師介紹","聯絡我們"],
           "nav_files": ["index.html","about.html","courses.html","teachers.html","contact.html"]},
    "en": {"name": "English", "dir": "en", "html_lang": "en",
           "nav": ["Home","About Us","Courses","Teachers","Contact"],
           "nav_files": ["index.html","about.html","courses.html","teachers.html","contact.html"]},
    "fr": {"name": "Français", "dir": "fr", "html_lang": "fr",
           "nav": ["Accueil","À propos","Cours","Professeurs","Contact"],
           "nav_files": ["index.html","about.html","courses.html","teachers.html","contact.html"]},
    "hi": {"name": "हिन्दी", "dir": "hi", "html_lang": "hi",
           "nav": ["होम","हमारे बारे में","पाठ्यक्रम","शिक्षक","संपर्क"],
           "nav_files": ["index.html","about.html","courses.html","teachers.html","contact.html"]},
    "id": {"name": "Bahasa Indonesia", "dir": "id", "html_lang": "id",
           "nav": ["Beranda","Tentang Kami","Kursus","Pengajar","Kontak"],
           "nav_files": ["index.html","about.html","courses.html","teachers.html","contact.html"]},
}

# ---- translated content blocks ----
T = {
"en": {
  "top_wa":"WhatsApp: phil.deng", "top_mail":"phoenixdkd@gmail.com",
  "home_title":"Mandarin School — Help Your Child Fall in Love with Chinese",
  "home_desc":"A professional Chinese language school offering courses for preschoolers, primary students and adults. Small classes, experienced teachers, flexible online video lessons. Contact us via WhatsApp or email today.",
  "brand_sub":"MANDARIN SCHOOL",
  "hero_eyebrow":"PROFESSIONAL CHINESE EDUCATION",
  "hero_h1":"Help Your Child <span class=\"hl\">Fall in Love with Chinese</span><br>Starting from the Very First Lesson",
  "hero_lead":"We offer structured Chinese courses for preschoolers, primary students and adults — small classes, experienced teachers, and flexible online video lessons that build confidence and interest.",
  "hero_cta1":"View Courses","hero_cta2":"WhatsApp Us",
  "badge1_n":"10+","badge1_l":"Years Teaching","badge2_n":"500+","badge2_l":"Graduates","badge3_n":"1:6","badge3_l":"Teacher Ratio",
  "why_title":"Why Choose Us",
  "why1_t":"Native-level Teachers","why1_d":"Experienced Mandarin teachers from diverse backgrounds.",
  "why2_t":"Leveled Courses","why2_d":"Tailored to age and proficiency.",
  "why3_t":"Interactive Teaching","why3_d":"Games, reading and speaking in every lesson.",
  "why4_t":"Learn Anytime","why4_d":"Online video lessons, available 24/7.",
  "courses_title":"Course Highlights",
  "courses_sub":"From early childhood to advanced learners, there is something for everyone",
  "c1_t":"Preschool Starter","c1_d":"Songs, stories and play to build language sense and interest for ages 3–6.",
  "c2_t":"Primary Chinese","c2_d":"Aligned with school curricula; strengthens reading, writing and speaking.",
  "c3_t":"Adult Practical","c3_d":"From pinyin to conversation; speak with confidence daily, at work and when travelling.",
  "c4_t":"HSK Prep","c4_d":"Structured preparation for the HSK exam with clear goals and visible progress.",
  "c5_t":"Reading & Writing","c5_d":"Classic reading and writing practice to build literacy and thinking.",
  "c6_t":"1-on-1 Tutoring","c6_d":"Customised to your goals — fast and focused.",
  "courses_cta":"Full Course List",
  "teach_title":"Meet Our Teachers",
  "teach_sub":"An experienced and passionate teaching team",
  "t1_t":"Ms. Lin","t1_r":"Head of Early Childhood","t1_d":"Ten years in early education, great at getting kids to speak through play.",
  "t2_t":"Mr. Chen","t2_r":"Lead Primary Teacher","t2_d":"Knows the local curriculum; loved by parents for reading & writing teaching.",
  "t3_t":"Ms. Wang","t3_r":"Adult Conversation Tutor","t3_d":"Business and daily Chinese; relaxed and practical classes.",
  "t4_t":"Ms. Li","t4_r":"HSK Specialist","t4_d":"Knows the exam inside out; guides students steadily to each HSK level.",
  "t5_t":"Ms. Zhang","t5_r":"Reading & Writing Tutor","t5_d":"Loves literature; inspires kids to express ideas and observe the world.",
  "t6_t":"Ms. Zhao","t6_r":"Online Class Host","t6_d":"Makes remote lessons just as lively and engaging.",
  "teach_cta":"View All Teachers",
  "contact_title":"Any Questions? Contact Us Directly",
  "contact_sub":"We are happy to help with courses, enrolment and scheduling",
  "wa_card_t":"WhatsApp Quick Chat","wa_card_s":"Fastest way to reach us",
  "mail_card_t":"Email Us","mail_card_s":"For detailed questions",
  "about_title":"About Us",
  "about_sub":"We believe language is a key that opens up the world",
  "a1_t":"Our Philosophy","a1_d":"Since founding, Mandarin School has held one belief: help every child fall in love with Chinese. We avoid rote memorisation, using fun, interactive, real-life methods so students build instinct and confidence naturally.",
  "a2_t":"Our Method","a2_d":"Small classes mean every student is seen. Lessons blend songs, stories, games and practice, levelled by age and proficiency for steady, enjoyable progress.",
  "a3_t":"Our Teachers","a3_d":"All teachers hold relevant qualifications and rich experience — warm, patient, and in continuous training for the best learning experience.",
  "a4_t":"Our Promise","a4_d":"Transparent communication, flexible arrangements, and respect for every family's expectations. Your child's progress is our greatest achievement.",
  "about_cta":"Explore Our Courses",
  "courses_page_title":"Course List",
  "courses_page_sub":"Levelled by age and goal — find the right class for you",
  "course_rows":[
    ("Pre","Preschool Starter","Songs, stories and play build language sense. Ages 3–6.","Small class","1–2 / week"),
    ("Pri","Primary Chinese","Aligned with school curricula; reading, writing, speaking.","Levelled","P1–P6"),
    ("Ad","Adult Practical","From pinyin to conversation; confident daily & work use.","Flexible","Online video"),
    ("HSK","HSK Preparation","Structured exam prep with visible progress.","Goal-based","Levels 1–6"),
    ("Rd","Reading & Writing","Classic reading and writing practice.","Age-grouped","Monthly theme"),
    ("1:1","1-on-1 Tutoring","Customised to your goals; focused and fast.","Tailored","Your time"),
  ],
  "courses_book":"Book a Trial via WhatsApp",
  "teach_page_title":"Teachers",
  "teach_page_sub":"An experienced and passionate teaching team",
  "contact_page_title":"Contact Us",
  "contact_page_sub":"For enrolment, courses or any questions, feel free to reach out",
  "ci1_t":"WhatsApp","ci1_v":WA_ID,
  "ci2_t":"Email","ci2_v":EMAIL,
  "ci3_t":"Service Hours","ci3_v":"Any time (24/7)",
  "ci4_t":"How We Teach","ci4_v":"Online video lessons",
  "form_title":"Leave Your Enquiry",
  "f_name":"Name","f_contact":"Contact (email or WhatsApp)","f_msg":"What you'd like to know",
  "f_submit":"Submit Enquiry","f_note":"We respect your privacy; details are only used to reply to this enquiry.",
  "footer_tag":"Helping every student love and learn Chinese. Small classes, professional teachers, flexible online video lessons.",
  "footer_quick":"Quick Links","footer_courses":"Courses","footer_contact":"Contact Us",
  "all_courses":["Preschool","Primary","Adult","HSK Prep"],
  "copyright":"© 2026 Mandarin School. All rights reserved.",
  "og_title":"Mandarin School — Help Your Child Fall in Love with Chinese",
  "og_desc":"A professional Chinese language school. Small classes, experienced teachers, flexible online video lessons.",
  "tw_title":"Mandarin School — Help Your Child Fall in Love with Chinese",
  "tw_desc":"A professional Chinese language school. Small classes, experienced teachers.",
},
"fr": {
  "top_wa":"WhatsApp : phil.deng", "top_mail":"phoenixdkd@gmail.com",
  "home_title":"École de Chinois — Faites aimer le chinois à votre enfant",
  "home_desc":"École de chinois professionnelle proposant des cours pour les jeunes enfants, les élèves du primaire et les adultes. Petits groupes, professeurs expérimentés, apprentissage en vidéo en ligne. Contactez-nous sur WhatsApp ou par e-mail.",
  "brand_sub":"ÉCOLE DE CHINOIS",
  "hero_eyebrow":"ENSEIGNEMENT PROFESSIONNEL DU CHINOIS",
  "hero_h1":"Faites aimer le chinois à votre enfant<br>dès <span class=\"hl\">la première leçon</span>",
  "hero_lead":"Nous proposons des cours de chinois structurés pour les jeunes enfants, les élèves du primaire et les adultes — petits groupes, professeurs expérimentés et options flexibles en vidéo en ligne.",
  "hero_cta1":"Voir les cours","hero_cta2":"WhatsApp",
  "badge1_n":"10+","badge1_l":"Ans d'enseignement","badge2_n":"500+","badge2_l":"Élèves","badge3_n":"1:6","badge3_l":"Ratio prof/élève",
  "why_title":"Pourquoi nous choisir",
  "why1_t":"Professeurs natifs","why1_d":"Des professeurs de chinois expérimentés d'horizons divers.",
  "why2_t":"Cours par niveaux","why2_d":"Adaptés à l'âge et au niveau.",
  "why3_t":"Enseignement interactif","why3_d":"Jeux, lecture et expression à chaque cours.",
  "why4_t":"Apprenez à tout moment","why4_d":"Cours en vidéo en ligne, 24h/24.",
  "courses_title":"Nos cours",
  "courses_sub":"De la petite enfance aux apprenants avancés, il y en a pour tous",
  "c1_t":"Éveil préscolaire","c1_d":"Chansons, histoires et jeux pour les 3–6 ans.",
  "c2_t":"Chinois primaire","c2_d":"Aligné sur le programme scolaire ; lecture, écriture, expression.",
  "c3_t":"Chinois adulte","c3_d":"Du pinyin à la conversation ; parlez en confiance.",
  "c4_t":"Prépa HSK","c4_d":"Préparation structurée de l'examen HSK.",
  "c5_t":"Lecture & écriture","c5_d":"Lecture de classiques et pratique de l'écriture.",
  "c6_t":"Cours particulier","c6_d":"Personnalisé selon vos objectifs.",
  "courses_cta":"Tous les cours",
  "teach_title":"Rencontrez nos professeurs",
  "teach_sub":"Une équipe expérimentée et passionnée",
  "t1_t":"Mme Lin","t1_r":"Responsable petite enfance","t1_d":"Dix ans en petite enfance, fait parler les enfants par le jeu.",
  "t2_t":"M. Chen","t2_r":"Professeur principal primaire","t2_d":"Connaît le programme local ; apprécié pour lecture et écriture.",
  "t3_t":"Mme Wang","t3_r":"Tutrice conversation adultes","t3_d":"Chinois des affaires et quotidien ; cours pratiques.",
  "t4_t":"Mme Li","t4_r":"Spécialiste HSK","t4_d":"Connaît l'examen ; guide vers chaque niveau HSK.",
  "t5_t":"Mme Zhang","t5_r":"Tutrice lecture & écriture","t5_d":"Aime la littérature ; inspire les enfants à s'exprimer.",
  "t6_t":"Mme Zhao","t6_r":"Animatrice en ligne","t6_d":"Rend les cours à distance vivants et engageants.",
  "teach_cta":"Voir tous les professeurs",
  "contact_title":"Des questions ? Contactez-nous",
  "contact_sub":"Nous aidons volontiers pour les cours, l'inscription et le planning",
  "wa_card_t":"WhatsApp","wa_card_s":"Le plus rapide",
  "mail_card_t":"E-mail","mail_card_s":"Pour le détail",
  "about_title":"À propos",
  "about_sub":"Nous croyons que la langue ouvre le monde",
  "a1_t":"Notre philosophie","a1_d":"Depuis sa création, l'école croit : faire aimer le chinois à chaque enfant. Pas de mémorisation brute, mais des méthodes ludiques et réelles qui créent la confiance.",
  "a2_t":"Notre méthode","a2_d":"Petits groupes où chaque élève est vu. Chansons, histoires, jeux et pratique, par niveaux.",
  "a3_t":"Nos professeurs","a3_d":"Tous qualifiés et expérimentés — chaleureux, patients, en formation continue.",
  "a4_t":"Notre promesse","a4_d":"Communication transparente, horaires flexibles, respect de chaque famille. Votre progrès est notre fierté.",
  "about_cta":"Découvrir nos cours",
  "courses_page_title":"Liste des cours",
  "courses_page_sub":"Par âge et objectif — trouvez le bon cours",
  "course_rows":[
    ("Pre","Éveil préscolaire","Chansons, histoires et jeux. 3–6 ans.","Petit groupe","1–2 / sem"),
    ("Pri","Chinois primaire","Aligné sur le programme scolaire.","Par niveaux","P1–P6"),
    ("Ad","Chinois adulte","Du pinyin à la conversation.","Flexible","Vidéo en ligne"),
    ("HSK","Prépa HSK","Préparation structurée de l'examen.","Par objectifs","Niveaux 1–6"),
    ("Rd","Lecture & écriture","Lecture de classiques et écriture.","Par âge","Thème mensuel"),
    ("1:1","Cours particulier","Personnalisé selon vos objectifs.","Sur mesure","Votre horaire"),
  ],
  "courses_book":"Réserver un essai sur WhatsApp",
  "teach_page_title":"Professeurs",
  "teach_page_sub":"Une équipe expérimentée et passionnée",
  "contact_page_title":"Contact",
  "contact_page_sub":"Inscription, cours ou questions — contactez-nous",
  "ci1_t":"WhatsApp","ci1_v":WA_ID,
  "ci2_t":"E-mail","ci2_v":EMAIL,
  "ci3_t":"Horaires","ci3_v":"À tout moment (24/7)",
  "ci4_t":"Modalité","ci4_v":"Cours en vidéo en ligne",
  "form_title":"Laissez votre message",
  "f_name":"Nom","f_contact":"Contact (e-mail ou WhatsApp)","f_msg":"Votre question",
  "f_submit":"Envoyer","f_note":"Nous respectons votre vie privée ; vos données servent uniquement à répondre.",
  "footer_tag":"Aider chaque élève à aimer et apprendre le chinois. Petits groupes, professeurs professionnels, flexibles.",
  "footer_quick":"Liens utiles","footer_courses":"Cours","footer_contact":"Contact",
  "all_courses":["Préscolaire","Primaire","Adulte","Prépa HSK"],
  "copyright":"© 2026 École de Chinois. Tous droits réservés.",
  "og_title":"École de Chinois — Faites aimer le chinois à votre enfant",
  "og_desc":"École de chinois professionnelle. Petits groupes, professeurs expérimentés, en vidéo en ligne.",
  "tw_title":"École de Chinois — Faites aimer le chinois à votre enfant",
  "tw_desc":"École de chinois professionnelle. Petits groupes, professeurs expérimentés.",
},
"hi": {
  "top_wa":"WhatsApp: phil.deng", "top_mail":"phoenixdkd@gmail.com",
  "home_title":"मैंडरिन स्कूल — अपने बच्चे को चीनी सीखना पसंद कराएँ",
  "home_desc":"एक पेशेवर चीनी भाषा स्कूल जो प्रीस्कूल, प्राथमिक और वयस्क छात्रों के लिए पाठ्यक्रम देता है। छोटे समूह, अनुभवी शिक्षक, ऑनलाइन वीडियो। WhatsApp या ईमेल से संपर्क करें।",
  "brand_sub":"मैंडरिन स्कूल",
  "hero_eyebrow":"पेशेवर चीनी शिक्षा",
  "hero_h1":"अपने बच्चे को चीनी सीखना <span class=\"hl\">पसंद कराएँ</span><br>पहली क्लास से शुरू",
  "hero_lead":"हम प्रीस्कूल, प्राथमिक और वयस्क छात्रों के लिए संरचित चीनी पाठ्यक्रम देते हैं — छोटे समूह, अनुभवी शिक्षक और लचीले विकल्प।",
  "hero_cta1":"कोर्स देखें","hero_cta2":"WhatsApp करें",
  "badge1_n":"10+","badge1_l":"वर्षों का अनुभव","badge2_n":"500+","badge2_l":"छात्र","badge3_n":"1:6","badge3_l":"अनुपात",
  "why_title":"हमें क्यों चुनें",
  "why1_t":"मातृभाषी शिक्षक","why1_d":"विविध पृष्ठभूमि के अनुभवी शिक्षक।",
  "why2_t":"स्तरीय कोर्स","why2_d":"उम्र और स्तर के अनुसार।",
  "why3_t":"इंटरैक्टिव पढ़ाई","why3_d":"हर क्लास में खेल और बातचीत।",
  "why4_t":"लचीला समय","why4_d":"ऑनलाइन वीडियो, आसान शेड्यूल।",
  "courses_title":"हमारे कोर्स",
  "courses_sub":"बचपन से लेकर उन्नत तक, सभी के लिए",
  "c1_t":"प्रीस्कूल आरंभ","c1_d":"3–6 वर्ष के बच्चों के लिए गीत और खेल।",
  "c2_t":"प्राथमिक चीनी","c2_d":"स्कूल पाठ्यक्रम के अनुरूप; पढ़ना, लिखना, बोलना।",
  "c3_t":"वयस्क चीनी","c3_d":"पिनयिन से बातचीत तक; आत्मविश्वास से बोलें।",
  "c4_t":"HSK तैयारी","c4_d":"संरचित HSK परीक्षा तैयारी।",
  "c5_t":"पठन और लेखन","c5_d":"क्लासिक पठन और लेखन अभ्यास।",
  "c6_t":"वन-ऑन-वन ट्यूशन","c6_d":"आपके लक्ष्य के अनुसार।",
  "courses_cta":"सभी कोर्स",
  "teach_title":"हमारे शिक्षकों से मिलें",
  "teach_sub":"अनुभवी और समर्पित टीम",
  "t1_t":"लिन जी","t1_r":"प्रीस्कूल प्रमुख","t1_d":"दस वर्ष का अनुभव, खेल से बच्चों को बोलना सिखाती हैं।",
  "t2_t":"चेन जी","t2_r":"प्राथमिक शिक्षक","t2_d":"स्थानीय पाठ्यक्रम जानते हैं; पढ़ने-लिखने में उत्कृष्ट।",
  "t3_t":"वांग जी","t3_r":"वयस्क बातचीत ट्यूटर","t3_d":"व्यावसायिक और दैनिक चीनी; व्यावहारिक क्लास।",
  "t4_t":"ली जी","t4_r":"HSK विशेषज्ञ","t4_d":"परीक्षा की गहरी समझ; हर स्तर तक मार्गदर्शन।",
  "t5_t":"झांग जी","t5_r":"पठन-लेखन ट्यूटर","t5_d":"साहित्य प्रेमी; बच्चों को अभिव्यक्ति सिखाती हैं।",
  "t6_t":"झाओ जी","t6_r":"ऑनलाइन शिक्षक","t6_d":"दूरस्थ क्लास को भी जीवंत बनाती हैं।",
  "teach_cta":"सभी शिक्षक देखें",
  "contact_title":"सवाल हैं? सीधे संपर्क करें",
  "contact_sub":"कोर्स, दाखिला और शेड्यूल में खुशी से मदद करेंगे",
  "wa_card_t":"WhatsApp","wa_card_s":"सबसे तेज़",
  "mail_card_t":"ईमेल","mail_card_s":"विस्तार के लिए",
  "about_title":"हमारे बारे में",
  "about_sub":"हम मानते हैं भाषा दुनिया की चाबी है",
  "a1_t":"हमारा दर्शन","a1_d":"स्थापना से ही हमारा विश्वास: हर बच्चे को चीनी सीखना पसंद हो। रटने के बजाय मज़ेदार तरीक़े अपनाते हैं।",
  "a2_t":"हमारी विधि","a2_d":"छोटे समूह; गीत, कहानी, खेल और अभ्यास, स्तर के अनुसार।",
  "a3_t":"हमारे शिक्षक","a3_d":"सभी योग्य और अनुभवी — गर्मजोशी और धैर्य के साथ।",
  "a4_t":"हमारा वादा","a4_d":"पारदर्शी संचार, लचीला समय, हर परिवार का सम्मान। आपकी प्रगति ही हमारी उपलब्धि है।",
  "about_cta":"कोर्स देखें",
  "courses_page_title":"कोर्स सूची",
  "courses_page_sub":"उम्र और लक्ष्य के अनुसार — सही क्लास चुनें",
  "course_rows":[
    ("Pre","प्रीस्कूल आरंभ","गीत और खेल। 3–6 वर्ष।","छोटा समूह","1–2 / सप्ताह"),
    ("Pri","प्राथमिक चीनी","स्कूल पाठ्यक्रम के अनुरूप।","स्तरीय","P1–P6"),
    ("Ad","वयस्क चीनी","पिनयिन से बातचीत।","लचीला","ऑनलाइन वीडियो"),
    ("HSK","HSK तैयारी","संरचित परीक्षा तैयारी।","लक्ष्य-आधारित","स्तर 1–6"),
    ("Rd","पठन और लेखन","क्लासिक पठन और लेखन।","उम्र के अनुसार","मासिक विषय"),
    ("1:1","वन-ऑन-वन","आपके लक्ष्य के अनुसार।","तैयार","आपका समय"),
  ],
  "courses_book":"WhatsApp से ट्रायल बुक करें",
  "teach_page_title":"शिक्षक",
  "teach_page_sub":"अनुभवी और समर्पित टीम",
  "contact_page_title":"संपर्क करें",
  "contact_page_sub":"दाखिला, कोर्स या कोई सवाल — बेझिझक लिखें",
  "ci1_t":"WhatsApp","ci1_v":WA_ID,
  "ci2_t":"ईमेल","ci2_v":EMAIL,
  "ci3_t":"समय","ci3_v":"किसी भी समय (24/7)",
  "ci4_t":"माध्यम","ci4_v":"ऑनलाइन वीडियो पाठ",
  "form_title":"अपना संदेश छोड़ें",
  "f_name":"नाम","f_contact":"संपर्क (ईमेल या WhatsApp)","f_msg":"आप क्या जानना चाहते हैं",
  "f_submit":"भेजें","f_note":"हम आपकी गोपनीयता का सम्मान करते हैं; जानकारी केवल जवाब देने के लिए।",
  "footer_tag":"हर छात्र को चीनी सीखना और पसंद करना। छोटे समूह, पेशेवर शिक्षक, लचीला।",
  "footer_quick":"त्वरित लिंक","footer_courses":"कोर्स","footer_contact":"संपर्क",
  "all_courses":["प्रीस्कूल","प्राथमिक","वयस्क","HSK"],
  "copyright":"© 2026 मैंडरिन स्कूल। सर्वाधिकार सुरक्षित।",
  "og_title":"मैंडरिन स्कूल — अपने बच्चे को चीनी सीखना पसंद कराएँ",
  "og_desc":"एक पेशेवर चीनी भाषा स्कूल। छोटे समूह, अनुभवी शिक्षक, ऑनलाइन वीडियो।",
  "tw_title":"मैंडरिन स्कूल — अपने बच्चे को चीनी सीखना पसंद कराएँ",
  "tw_desc":"एक पेशेवर चीनी भाषा स्कूल। छोटे समूह, अनुभवी शिक्षक।",
},
"id": {
  "top_wa":"WhatsApp: phil.deng", "top_mail":"phoenixdkd@gmail.com",
  "home_title":"Sekolah Mandarin — Buat Anak Mencintai Bahasa Mandarin",
  "home_desc":"Sekolah bahasa Mandarin profesional dengan kursus untuk anak prasekolah, sekolah dasar dan dewasa. Kelas kecil, guru berpengalaman, belajar video daring. Hubungi kami via WhatsApp atau email.",
  "brand_sub":"SEKOLAH MANDARIN",
  "hero_eyebrow":"PENDIDIKAN MANDARIN PROFESIONAL",
  "hero_h1":"Buat Anak Mencintai Bahasa Mandarin<br>mulai dari <span class=\"hl\">pelajaran pertama</span>",
  "hero_lead":"Kami menawarkan kursus Mandarin terstruktur untuk anak prasekolah, sekolah dasar dan dewasa — kelas kecil, guru berpengalaman, dan opsi video daring yang fleksibel.",
  "hero_cta1":"Lihat Kursus","hero_cta2":"WhatsApp Kami",
  "badge1_n":"10+","badge1_l":"Tahun Mengajar","badge2_n":"500+","badge2_l":"Lulusan","badge3_n":"1:6","badge3_l":"Rasio Guru",
  "why_title":"Mengapa Memilih Kami",
  "why1_t":"Guru Penutur Asli","why1_d":"Guru Mandarin berpengalaman dari berbagai latar belakang.",
  "why2_t":"Kursus Bertingkat","why2_d":"Sesuai usia dan kemampuan.",
  "why3_t":"Pengajaran Interaktif","why3_d":"Permainan, membaca dan berbicara di setiap kelas.",
  "why4_t":"Belajar Kapan Saja","why4_d":"Kursus video daring, 24/7.",
  "courses_title":"Kursus Kami",
  "courses_sub":"Dari anak usia dini hingga lanjutan, ada untuk semua",
  "c1_t":"Prasekolah","c1_d":"Lagu, cerita dan bermain untuk usia 3–6 tahun.",
  "c2_t":"Mandarin Dasar","c2_d":"Selaras kurikulum sekolah; membaca, menulis, berbicara.",
  "c3_t":"Mandarin Dewasa","c3_d":"Dari pinyin ke percakapan; percaya diri berbicara.",
  "c4_t":"Persiapan HSK","c4_d":"Persiapan ujian HSK terstruktur.",
  "c5_t":"Membaca & Menulis","c5_d":"Membaca klasik dan latihan menulis.",
  "c6_t":"Bimbingan 1-on-1","c6_d":"Sesuai tujuan Anda; fokus dan cepat.",
  "courses_cta":"Semua Kursus",
  "teach_title":"Kenali Guru Kami",
  "teach_sub":"Tim pengajar yang berpengalaman dan bersemangat",
  "t1_t":"Ibu Lin","t1_r":"Kepala Prasekolah","t1_d":"Sepuluh tahun di pendidikan anak; mahir membuat anak berbicara lewat bermain.",
  "t2_t":"Bpk Chen","t2_r":"Guru Dasar Utama","t2_d":"Memahami kurikulum lokal; disukai untuk membaca & menulis.",
  "t3_t":"Ibu Wang","t3_r":"Tutor Percakapan Dewasa","t3_d":"Mandarin bisnis dan harian; kelas praktis.",
  "t4_t":"Ibu Li","t4_r":"Spesialis HSK","t4_d":"Memahami ujian; membimbing ke setiap level HSK.",
  "t5_t":"Ibu Zhang","t5_r":"Tutor Membaca & Menulis","t5_d":"Mencintai sastra; menginspirasi anak menyatakan ide.",
  "t6_t":"Ibu Zhao","t6_r":"Host Kelas Daring","t6_d":"Membuat kelas daring tetap hidup dan seru.",
  "teach_cta":"Lihat Semua Guru",
  "contact_title":"Ada Pertanyaan? Hubungi Kami",
  "contact_sub":"Senang membantu kursus, pendaftaran dan jadwal",
  "wa_card_t":"WhatsApp","wa_card_s":"Cara tercepat",
  "mail_card_t":"Email","mail_card_s":"Untuk detail",
  "about_title":"Tentang Kami",
  "about_sub":"Kami percaya bahasa adalah kunci membuka dunia",
  "a1_t":"Filosofi Kami","a1_d":"Sejak berdiri, Sekolah Mandarin memegang satu keyakinan: membuat setiap anak mencintai bahasa Mandarin. Bukan hafalan, tapi cara menyenangkan dan nyata.",
  "a2_t":"Metode Kami","a2_d":"Kelas kecil agar setiap siswa terlihat. Lagu, cerita, permainan dan praktik, bertingkat.",
  "a3_t":"Guru Kami","a3_d":"Semua guru berkualifikasi dan berpengalaman — hangat, sabar, terus dilatih.",
  "a4_t":"Janji Kami","a4_d":"Komunikasi transparan, jadwal fleksibel, menghargai setiap keluarga. Kemajuan Anda adalah prestasi kami.",
  "about_cta":"Jelajahi Kursus",
  "courses_page_title":"Daftar Kursus",
  "courses_page_sub":"Bertingkat per usia dan tujuan — temukan kelas yang tepat",
  "course_rows":[
    ("Pre","Prasekolah","Lagu, cerita dan bermain. Usia 3–6.","Kelas kecil","1–2 / minggu"),
    ("Pri","Mandarin Dasar","Selaras kurikulum sekolah.","Bertingkat","P1–P6"),
    ("Ad","Mandarin Dewasa","Dari pinyin ke percakapan.","Fleksibel","Video daring"),
    ("HSK","Persiapan HSK","Persiapan ujian terstruktur.","Berdasarkan tujuan","Level 1–6"),
    ("Rd","Membaca & Menulis","Membaca klasik dan menulis.","Per usia","Tema bulanan"),
    ("1:1","Bimbingan 1-on-1","Sesuai tujuan Anda.","Kustom","Waktu Anda"),
  ],
  "courses_book":"Booking Trial via WhatsApp",
  "teach_page_title":"Guru",
  "teach_page_sub":"Tim pengajar yang berpengalaman dan bersemangat",
  "contact_page_title":"Kontak",
  "contact_page_sub":"Pendaftaran, kursus atau pertanyaan — silakan hubungi",
  "ci1_t":"WhatsApp","ci1_v":WA_ID,
  "ci2_t":"Email","ci2_v":EMAIL,
  "ci3_t":"Jam Layanan","ci3_v":"Kapan saja (24/7)",
  "ci4_t":"Cara Belajar","ci4_v":"Kursus video daring",
  "form_title":"Tinggalkan Pertanyaan",
  "f_name":"Nama","f_contact":"Kontak (email atau WhatsApp)","f_msg":"Yang ingin Anda tanyakan",
  "f_submit":"Kirim","f_note":"Kami menjaga privasi Anda; data hanya untuk membalas pertanyaan ini.",
  "footer_tag":"Membantu setiap siswa mencintai dan belajar Mandarin. Kelas kecil, guru profesional, fleksibel.",
  "footer_quick":"Tautan Cepat","footer_courses":"Kursus","footer_contact":"Kontak",
  "all_courses":["Prasekolah","Dasar","Dewasa","Persiapan HSK"],
  "copyright":"© 2026 Sekolah Mandarin. Hak cipta dilindungi.",
  "og_title":"Sekolah Mandarin — Buat Anak Mencintai Bahasa Mandarin",
  "og_desc":"Sekolah bahasa Mandarin profesional. Kelas kecil, guru berpengalaman, video daring.",
  "tw_title":"Sekolah Mandarin — Buat Anak Mencintai Bahasa Mandarin",
  "tw_desc":"Sekolah bahasa Mandarin profesional. Kelas kecil, guru berpengalaman.",
},
}

PAGES = ["index","about","courses","teachers","contact"]

def lang_switch(current_code, current_dir):
    """Build language switcher. current_dir '' for zh (root), else 'en' etc."""
    # compute prefix for links within the SAME language
    base = "" if current_dir == "" else f"/{current_dir}"
    out = []
    for code, meta in LANGS.items():
        target_dir = meta["dir"]
        if target_dir == "":
            href = base + "/" if base else "/"
        else:
            href = base + "/" if base else f"/{target_dir}/"
        # but we want to switch language while staying on same page
        # simpler: link to language root (or page). Use same page name:
        page_part = ""  # default to language home
        if href.endswith("/"):
            href = href.rstrip("/")
        active = " active" if code == current_code else ""
        out.append(f'        <a class="{code}{active}" href="{href}">{meta["name"]}</a>')
    return "\n".join(out)

def hreflang_tags(current_dir):
    """Generate hreflang + canonical for the page. dir '' for zh."""
    page = PAGES  # placeholder; built per page below
    return ""

def build_hreflang(dirs_map, current_dir, page_file):
    """dirs_map: list of (code, dir) ; current_dir is this page's dir."""
    lines = []
    for code, d in dirs_map:
        if d == "":
            url = f"{DOMAIN}/{page_file}"
        else:
            url = f"{DOMAIN}/{d}/{page_file}"
        lines.append(f'  <link rel="alternate" hreflang="{LANGS[code]["html_lang"].split("-")[0]}" href="{url}" />')
    # x-default -> chinese (root)
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{DOMAIN}/{page_file}" />')
    return "\n".join(lines)

# map code->dir
DIRS_MAP = [(c, LANGS[c]["dir"]) for c in LANGS]

def topbar(t, wa_href):
    return f'''  <div class="topbar">
    <div class="container">
      <div class="tb-left">
        <span class="tb-item">
          <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Z"/></svg>
          <a href="{wa_href}" target="_blank" rel="noopener">WhatsApp：{WA_ID}</a>
        </span>
        <span class="tb-item">
          <svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5-8-5V6l8 5 8-5v2Z"/></svg>
          <a href="{MAILTO}">{EMAIL}</a>
        </span>
      </div>
    </div>
  </div>'''

def header(t, code, cur_dir, page_file):
    nav = LANGS[code]["nav"]
    files = LANGS[code]["nav_files"]
    nav_html = "\n".join(
        '        <a href="' + ('.' if cur_dir=="" else '..') + '/' + f + ('" class="active"' if f==page_file else '"') + '>' + n + '</a>'
        for n, f in zip(nav, files)
    )
    # language switch in header
    ls_items = []
    for c, meta in LANGS.items():
        d = meta["dir"]
        # same page, other language
        other_page = page_file if d != "" else page_file
        if d == "":
            href = f"/{page_file}"
        else:
            href = f"/{d}/{page_file}"
        active = " active" if c == code else ""
        ls_items.append(f'      <a class="{c}{active}" href="{href}">{meta["name"]}</a>')
    ls = "\n".join(ls_items)
    return f'''  <header class="header">
    <div class="container">
      <a class="brand" href="{"." if cur_dir=="" else ".."}/index.html"><span class="logo">華</span><span>{BRAND}<small>{t["brand_sub"]}</small></span></a>
      <nav class="nav">
{nav_html}
      </nav>
      <div class="lang-switch">
{ls}
      </div>
      <button class="nav-toggle" id="navToggle" aria-label="選單"><span></span><span></span><span></span></button>
    </div>
  </header>
  <div class="mobile-menu" id="mobileMenu">
{nav_html}
    <div class="lang-switch">
{ls}
    </div>
  </div>'''

def footer(t, code, cur_dir):
    up = "." if cur_dir=="" else ".."
    quick = "\n".join(
        f'        <li><a href="{up}/{f}">{n}</a></li>' for n,f in zip(LANGS[code]["nav"], LANGS[code]["nav_files"])
    )
    courses = "\n".join(f'        <li><a href="{up}/courses.html">{c}</a></li>' for c in t["all_courses"])
    return f'''  <footer class="footer">
    <div class="container">
      <div class="cols">
        <div>
          <div class="brand-f"><span class="logo">華</span>{BRAND}</div>
          <p>{t["footer_tag"]}</p>
        </div>
        <div><h4>{t["footer_quick"]}</h4><ul class="fl">
{quick}
        </ul></div>
        <div><h4>{t["footer_courses"]}</h4><ul class="fl">
{courses}
        </ul></div>
        <div><h4>{t["footer_contact"]}</h4><ul class="fl">
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp：{WA_ID}</a></li>
          <li><a href="{MAILTO}">{EMAIL}</a></li>
          <li><a href="{up}/contact.html">{t["footer_contact"]}</a></li>
        </ul></div>
      </div>
      <div class="footer-bottom">{t["copyright"]}</div>
    </div>
  </footer>'''

def head_block(t, code, cur_dir, page_file, page_title, page_desc, jsonld):
    up = "." if cur_dir=="" else ".."
    url = f"{DOMAIN}/{page_file}" if cur_dir=="" else f"{DOMAIN}/{cur_dir}/{page_file}"
    hl = build_hreflang(DIRS_MAP, cur_dir, page_file)
    return f'''  <title>{page_title}</title>
  <meta name="description" content="{page_desc}" />
  <link rel="canonical" href="{url}" />
{hl}
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="{BRAND} {BRAND_EN}" />
  <meta property="og:title" content="{t["og_title"]}" />
  <meta property="og:description" content="{t["og_desc"]}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{DOMAIN}/assets/img/og-image.png" />
  <meta property="og:locale" content="{LANGS[code]["html_lang"]}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t["tw_title"]}" />
  <meta name="twitter:description" content="{t["tw_desc"]}" />
  <meta name="twitter:image" content="{DOMAIN}/assets/img/og-image.png" />
  <link rel="icon" type="image/svg+xml" href="{up}/assets/img/favicon.svg" />
  <link rel="stylesheet" href="{up}/assets/css/style.css" />
  <script type="application/ld+json">
  {jsonld}
  </script>'''

def jsonld_school(t, url):
    return json.dumps({
        "@context":"https://schema.org","@type":"School",
        "name":f"{BRAND} {BRAND_EN}","url":url,
        "description":t["home_desc"],"email":EMAIL,"telephone":f"+852 {WA_ID}",
        "address":{"@type":"PostalAddress","addressCountry":"HK"}
    }, ensure_ascii=False, indent=2)

def jsonld_generic(t, ptype, url, desc):
    return json.dumps({
        "@context":"https://schema.org","@type":ptype,
        "name":t.get("home_title",BRAND),"url":url,"description":desc
    }, ensure_ascii=False, indent=2)

# ---- build a full page ----
def build_page(code, page, t):
    cur_dir = LANGS[code]["dir"]
    up = "." if cur_dir=="" else ".."
    files = LANGS[code]["nav_files"]
    page_file = files[PAGES.index(page)]
    wa_href = WA
    # page-specific body
    if page == "index":
        body = f'''  <section class="hero">
    <div class="container">
      <div>
        <span class="eyebrow">{t["hero_eyebrow"]}</span>
        <h1>{t["hero_h1"]}</h1>
        <p class="lead">{t["hero_lead"]}</p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="{up}/courses.html">{t["hero_cta1"]}</a>
          <a class="btn btn-ghost btn-lg" href="{wa_href}" target="_blank" rel="noopener">{t["hero_cta2"]}</a>
        </div>
        <div class="hero-badges">
          <div class="b"><b>{t["badge1_n"]}</b><span>{t["badge1_l"]}</span></div>
          <div class="b"><b>{t["badge2_n"]}</b><span>{t["badge2_l"]}</span></div>
          <div class="b"><b>{t["badge3_n"]}</b><span>{t["badge3_l"]}</span></div>
        </div>
      </div>
      <aside class="hero-card">
        <h3>{t["why_title"]}</h3>
        <div class="row"><span class="ic">語</span><div><b>{t["why1_t"]}</b><span>{t["why1_d"]}</span></div></div>
        <div class="row"><span class="ic">課</span><div><b>{t["why2_t"]}</b><span>{t["why2_d"]}</span></div></div>
        <div class="row"><span class="ic">活</span><div><b>{t["why3_t"]}</b><span>{t["why3_d"]}</span></div></div>
        <div class="row"><span class="ic">便</span><div><b>{t["why4_t"]}</b><span>{t["why4_d"]}</span></div></div>
      </aside>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 class="section-title">{t["courses_title"]}</h2>
      <p class="section-sub">{t["courses_sub"]}</p>
      <div class="grid grid-3">
        <div class="card"><div class="ic-xl">{t["c1_t"][0]}</div><h3>{t["c1_t"]}</h3><p>{t["c1_d"]}</p></div>
        <div class="card"><div class="ic-xl">{t["c2_t"][0]}</div><h3>{t["c2_t"]}</h3><p>{t["c2_d"]}</p></div>
        <div class="card"><div class="ic-xl">{t["c3_t"][0]}</div><h3>{t["c3_t"]}</h3><p>{t["c3_d"]}</p></div>
        <div class="card"><div class="ic-xl">{t["c4_t"][0]}</div><h3>{t["c4_t"]}</h3><p>{t["c4_d"]}</p></div>
        <div class="card"><div class="ic-xl">{t["c5_t"][0]}</div><h3>{t["c5_t"]}</h3><p>{t["c5_d"]}</p></div>
        <div class="card"><div class="ic-xl">{t["c6_t"][0]}</div><h3>{t["c6_t"]}</h3><p>{t["c6_d"]}</p></div>
      </div>
      <div style="text-align:center;margin-top:34px;">
        <a class="btn btn-gold btn-lg" href="{up}/courses.html">{t["courses_cta"]}</a>
      </div>
    </div>
  </section>

  <section class="section alt">
    <div class="container">
      <h2 class="section-title">{t["teach_title"]}</h2>
      <p class="section-sub">{t["teach_sub"]}</p>
      <div class="grid grid-3">
        <div class="teacher"><div class="avatar">{t["t1_t"][0]}</div><h3>{t["t1_t"]}</h3><div class="role">{t["t1_r"]}</div><p>{t["t1_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t2_t"][0]}</div><h3>{t["t2_t"]}</h3><div class="role">{t["t2_r"]}</div><p>{t["t2_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t3_t"][0]}</div><h3>{t["t3_t"]}</h3><div class="role">{t["t3_r"]}</div><p>{t["t3_d"]}</p></div>
      </div>
      <div style="text-align:center;margin-top:34px;">
        <a class="btn btn-ghost btn-lg" href="{up}/teachers.html">{t["teach_cta"]}</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 class="section-title">{t["contact_title"]}</h2>
      <p class="section-sub">{t["contact_sub"]}</p>
      <div class="contact-direct">
        <div class="direct-card wa">
          <span class="ic">💬</span>
          <div><b>{t["wa_card_t"]}</b><small>{t["wa_card_s"]}</small><br/><a href="{wa_href}" target="_blank" rel="noopener">{WA_ID}</a></div>
        </div>
        <div class="direct-card mail">
          <span class="ic">✉️</span>
          <div><b>{t["mail_card_t"]}</b><small>{t["mail_card_s"]}</small><br/><a href="{MAILTO}">{EMAIL}</a></div>
        </div>
      </div>
    </div>
  </section>'''
        jsonld = jsonld_school(t, f"{DOMAIN}/{page_file}" if cur_dir=="" else f"{DOMAIN}/{cur_dir}/{page_file}")
        ptitle = t["home_title"]; pdesc = t["home_desc"]
    elif page == "about":
        body = f'''  <section class="section">
    <div class="container">
      <h2 class="section-title">{t["about_title"]}</h2>
      <p class="section-sub">{t["about_sub"]}</p>
      <div class="grid grid-2">
        <div class="card"><h3>{t["a1_t"]}</h3><p>{t["a1_d"]}</p></div>
        <div class="card"><h3>{t["a2_t"]}</h3><p>{t["a2_d"]}</p></div>
        <div class="card"><h3>{t["a3_t"]}</h3><p>{t["a3_d"]}</p></div>
        <div class="card"><h3>{t["a4_t"]}</h3><p>{t["a4_d"]}</p></div>
      </div>
      <div style="text-align:center;margin-top:36px;">
        <a class="btn btn-primary btn-lg" href="{up}/courses.html">{t["about_cta"]}</a>
      </div>
    </div>
  </section>'''
        jsonld = jsonld_generic(t, "AboutPage", f"{DOMAIN}/{cur_dir+'/' if cur_dir else ''}{page_file}", t["about_sub"])
        ptitle = t["about_title"]; pdesc = t["about_sub"]
    elif page == "courses":
        rows = ""
        for tag, name, desc, meta, when in t["course_rows"]:
            rows += f'''        <div class="course">
          <span class="tag">{tag}</span>
          <div><h3>{name}</h3><p>{desc}</p></div>
          <div class="meta"><div class="price">{meta}</div><div class="when">{when}</div></div>
        </div>
'''
        body = f'''  <section class="section">
    <div class="container">
      <h2 class="section-title">{t["courses_page_title"]}</h2>
      <p class="section-sub">{t["courses_page_sub"]}</p>
      <div class="grid" style="gap:18px;">
{rows}      </div>
      <div style="text-align:center;margin-top:36px;">
        <a class="btn btn-gold btn-lg" href="{wa_href}" target="_blank" rel="noopener">{t["courses_book"]}</a>
      </div>
    </div>
  </section>'''
        jsonld = jsonld_generic(t, "ItemList", f"{DOMAIN}/{cur_dir+'/' if cur_dir else ''}{page_file}", t["courses_page_sub"])
        ptitle = t["courses_page_title"]; pdesc = t["courses_page_sub"]
    elif page == "teachers":
        body = f'''  <section class="section">
    <div class="container">
      <h2 class="section-title">{t["teach_page_title"]}</h2>
      <p class="section-sub">{t["teach_page_sub"]}</p>
      <div class="grid grid-3">
        <div class="teacher"><div class="avatar">{t["t1_t"][0]}</div><h3>{t["t1_t"]}</h3><div class="role">{t["t1_r"]}</div><p>{t["t1_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t2_t"][0]}</div><h3>{t["t2_t"]}</h3><div class="role">{t["t2_r"]}</div><p>{t["t2_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t3_t"][0]}</div><h3>{t["t3_t"]}</h3><div class="role">{t["t3_r"]}</div><p>{t["t3_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t4_t"][0]}</div><h3>{t["t4_t"]}</h3><div class="role">{t["t4_r"]}</div><p>{t["t4_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t5_t"][0]}</div><h3>{t["t5_t"]}</h3><div class="role">{t["t5_r"]}</div><p>{t["t5_d"]}</p></div>
        <div class="teacher"><div class="avatar">{t["t6_t"][0]}</div><h3>{t["t6_t"]}</h3><div class="role">{t["t6_r"]}</div><p>{t["t6_d"]}</p></div>
      </div>
    </div>
  </section>'''
        jsonld = jsonld_generic(t, "Organization", f"{DOMAIN}/{cur_dir+'/' if cur_dir else ''}{page_file}", t["teach_page_sub"])
        ptitle = t["teach_page_title"]; pdesc = t["teach_page_sub"]
    elif page == "contact":
        body = f'''  <section class="section">
    <div class="container">
      <h2 class="section-title">{t["contact_page_title"]}</h2>
      <p class="section-sub">{t["contact_page_sub"]}</p>
      <div class="contact-grid">
        <div class="contact-info">
          <div class="ci"><span class="ic">💬</span><div><b>{t["ci1_t"]}</b><a href="{wa_href}" target="_blank" rel="noopener">{WA_ID}</a></div></div>
          <div class="ci"><span class="ic">✉️</span><div><b>{t["ci2_t"]}</b><a href="{MAILTO}">{EMAIL}</a></div></div>
          <div class="ci"><span class="ic">🕘</span><div><b>{t["ci3_t"]}</b><span>{t["ci3_v"]}</span></div></div>
          <div class="ci"><span class="ic">📍</span><div><b>{t["ci4_t"]}</b><span>{t["ci4_v"]}</span></div></div>
        </div>
        <form class="form-card" onsubmit="return false;">
          <h3 style="margin-top:0;">{t["form_title"]}</h3>
          <label for="name">{t["f_name"]}</label>
          <input id="name" type="text" placeholder="{t["f_name"]}" />
          <label for="email">{t["f_contact"]}</label>
          <input id="email" type="text" placeholder="{EMAIL} / {WA_ID}" />
          <label for="msg">{t["f_msg"]}</label>
          <textarea id="msg" placeholder="{t["f_msg"]}"></textarea>
          <button class="btn btn-primary btn-lg" type="submit" style="margin-top:18px;width:100%;justify-content:center;" onclick="alert('{t['f_submit']}!');">{t["f_submit"]}</button>
          <p class="form-note">{t["f_note"]}</p>
        </form>
      </div>
      <div class="contact-direct">
        <div class="direct-card wa">
          <span class="ic">💬</span>
          <div><b>{t["wa_card_t"]}</b><small>{t["wa_card_s"]}</small><br/><a href="{wa_href}" target="_blank" rel="noopener">{WA_ID}</a></div>
        </div>
        <div class="direct-card mail">
          <span class="ic">✉️</span>
          <div><b>{t["mail_card_t"]}</b><small>{t["mail_card_s"]}</small><br/><a href="{MAILTO}">{EMAIL}</a></div>
        </div>
      </div>
    </div>
  </section>'''
        jsonld = jsonld_generic(t, "ContactPage", f"{DOMAIN}/{cur_dir+'/' if cur_dir else ''}{page_file}", t["contact_page_sub"])
        ptitle = t["contact_page_title"]; pdesc = t["contact_page_sub"]

    doc = f'''<!DOCTYPE html>
<html lang="{LANGS[code]["html_lang"]}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
{head_block(t, code, cur_dir, page_file, ptitle, pdesc, jsonld)}
</head>
<body>
{topbar(t, wa_href)}
{header(t, code, cur_dir, page_file)}
{body}
{footer(t, code, cur_dir)}
  <script src="{up}/assets/js/main.js"></script>
</body>
</html>'''
    return doc

# ---- generate ----
for code in ["en","fr","hi","id"]:
    t = T[code]
    d = LANGS[code]["dir"]
    outdir = os.path.join(ROOT, d)
    os.makedirs(outdir, exist_ok=True)
    for page in PAGES:
        doc = build_page(code, page, t)
        with open(os.path.join(outdir, f"{page}.html"), "w", encoding="utf-8") as f:
            f.write(doc)
    print(f"generated {d}/ : {PAGES}")

print("DONE")
