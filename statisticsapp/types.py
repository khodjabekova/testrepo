from enum import Enum


class FinanceEntityType(Enum):
    xorijiy_eksportlar = ["Xorijiy ekspertlar (sohalar kesimida)", "Хорижий экспертлар (соҳалар кесимида)",
                          "Зарубежные эксперты (по отраслям)", "Foreign experts (by industry)"]
    noyob_qolyozmalar = ["Noyob qo‘lyozmalar", "Ноёб қўлёзмалар", "Уникальные рукописи", "Unique Manuscripts"]
    bazadan_foydalanish = ["Ilmiy-tadqiqot va oliy ta’lim muassasalarining yetakchi elektron ilmiy ma’lumotlar bazalaridan erkin foydalanishni ta’minlash",
                           "Илмий-тадқиқот ва олий таълим муассасаларининг йетакчи електрон илмий маълумотлар базаларидан еркин фойдаланишни таъминлаш",
                           "Обеспечение свободного доступа к ведущим электронным научным базам научно-исследовательских и высших учебных заведений",
                           "Ensuring free access to leading electronic scientific databases of research and higher education institutions"]
    orolboyi_markazi = ["Ilmiy-tadqiqot va oliy ta’lim muassasalarining xalqaro nashrlarda ilmiy natijalarni chop etishga tayyorlash",
                        "Илмий-тадқиқот ва олий таълим муассасаларининг халқаро нашрларда илмий натижаларни чоп етишга тайёрлаш",
                        "Подготовка научно-исследовательских и высших учебных заведений к публикации научных результатов в международных изданиях",
                        "Preparation of research and higher education institutions for publication of scientific results in international publications"]