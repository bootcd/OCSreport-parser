import os



def createPage(filename, cpu_dict, ram_dict, storage_dict ):
    work_dir = os.getenv("USERPROFILE") + "\html\\"
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    f = open(work_dir + filename + ".html", "w+")
    f.write(
        "<!DOCTYPE html PUBLIC '"'-//W3C//DTD HTML 4.01//EN'"' '"'http://www.w3.org/TR/html4/strict.dtd'"'>\r\n")
    f.write("<html>\r\n")
    f.write("<head>\r\n")
    f.write(
        "<meta content='"'text/html; charset=windows1251'"' http-equiv='"'content-type'"'><title>ARMPassport</title>\r\n")
    f.write("</head>\r\n")
    f.write("<body>\r\n")
    f.write(
        "<table style='"'text-align: left; width: 100%;'"' border='"'1'"' "
        "cellpadding='"'2'"' cellspacing='"'2'"'>\r\n")
    f.write("<tbody>\r\n")
    f.write("<tr>\r\n")
    f.write(
        "<th style='"'text-align: center; vertical-align: middle;'"'>"
        "Паспорт автоматизированного рабочего места (" + filename + ")</th>\r\n")
    f.write("</tr>\r\n")
    f.write("</tbody>\r\n")
    f.write("</table>\r\n")
    f.write("<br>\r\n")
    f.write(
        "<table style='"'text-align: left; width: 30%;'"' border='"'1'"' "
        "cellpadding='"'2'"' cellspacing='"'2'"'>\r\n")
    f.write("<tbody>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>ФИО</td>\r\n")
    f.write("<td style='"'width: 143px;'"'>UNKNOWN_USER\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Кабинет</td>\r\n")
    f.write("<td style='"'width: 143px;'"'>NOT_SET\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Логин в домене</td>\r\n")
    f.write("<td style='"'width: 143px;'"'>NO_DOMAIN_LOGIN\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("</tbody>\r\n")
    f.write("</table>\r\n")
    f.write("<br>\r\n")
    f.write(
        "<table style='"'text-align: left; width: 100%;'"' border='"'1'"'"
        " cellpadding='"'2'"' cellspacing='"'2'"'>\r\n")
    f.write("<tbody>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'text-align: center; vertical-align: middle;'"'>Аппаратное обеспечение</td>\r\n")
    f.write("</tr>\r\n")
    f.write("</tbody>\r\n")
    f.write("</table>\r\n")
    f.write("<br>\r\n")
    f.write(
        "<table style='"'text-align: left; width: 100%;'"' border='"'1'"' "
        "cellpadding='"'2'"' cellspacing='"'2'"'>\r\n")
    f.write("<tbody>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Процессор</td>\r\n")
    cpunamestr = "<td style='"'width: 833px;'"'>" + \
                 format(''.join(cpu_dict['name'])) + ", количество ядер: " + \
                 format(''.join(cpu_dict['corenumber'])) + ", сокет: " + \
                 format(''.join(cpu_dict['cpusocket'])) + ", архитектура: " + \
                 format(''.join(cpu_dict['cpuarch'])) + ", " + \
                 format(cpu_dict['cpunumber']) + " шт" + "\r\n"
    f.write(cpunamestr)
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Память</td>\r\n")
    f.write("<td style='"'width: 833px;'"'>" + "Всего: " +
            format(ram_dict['ram_size_summary']) + ",  количество слотов: " +
            format(ram_dict['slots_number']) + ",  объем по слотам: " +
            format(', '.join(ram_dict['size_in_slot'])) + ",  тип: " +
            format(''.join(ram_dict['type'])) + ",  частота: " +
            format(''.join(ram_dict['freq'])) + "МГц" + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Накопитель</td>\r\n")

    f.write("<td style='"'width: 833px;'"'>" + format(', '.join(storage_dict['device %d' % i])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Видеоадаптер</td>\r\n")
    f.write("<td style='"'width: 833px;'"'>" + format(''.join(video_dict['name'])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Аппаратный адрес (mac)</td>\r\n")
    f.write("<td style='"'width: 833px;'"'>" + format(''.join(networks_dict['macaddrres'])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 133px;'"'>Монитор:</td>\r\n")
    f.write("<td style='"'width: 833px;'"'>" + format(''.join(monitor_dict['name'])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("</tbody>\r\n")
    f.write("</table>\r\n")
    f.write("<br>\r\n")
    f.write(
        "<table style='"'text-align: left; width: 100%;'"' border='"'1'"'"
        " cellpadding='"'2'"' cellspacing='"'2'"'>\r\n")
    f.write("<tbody>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'text-align: center;'"'>Программное обеспечение</td>\r\n")
    f.write("</tr>\r\n")
    f.write("</tbody>\r\n")
    f.write("</table>\r\n")
    f.write("<br>\r\n")
    f.write(
        "<table style='"'text-align: left; width: 100%;'"' border='"'1'"'"
        " cellpadding='"'2'"' cellspacing='"'2'"'>\r\n")
    f.write("<tbody>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 229px;'"'>Операционная система</td>\r\n")
    f.write("<td style='"'width: 707px;'"'>" + format(''.join(osparams_dict['name'])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 229px;'"'>Офисный пакет</td>\r\n")
    f.write("<td style='"'width: 707px;'"'>" + format(''.join(office_dict['name'][1])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 229px;'"'>Антивирус</td>\r\n")
    f.write("<td style='"'width: 707px;'"'>" + format(''.join(avir_dict['name'])) + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("<tr>\r\n")
    f.write("<td style='"'width: 229px;'"'>ПО с коммерческой лицензией</td>\r\n")
    f.write("<td style='"'width: 707px;'"'>" + "UNKNOWN_LICENSES" + "\r\n")
    f.write("</td>\r\n")
    f.write("</tr>\r\n")
    f.write("</tbody>\r\n")
    f.write("</table>\r\n")
    f.write("<br>\r\n")
    f.write("<br>\r\n")
    f.write("<br>\r\n")
    f.write("<br>\r\n")
    f.write("<br>\r\n")
    f.write("<br>\r\n")
    f.write("<br>\r\n")
    f.write("</body>\r\n")
    f.write("</html>\r\n")
    f.close()


