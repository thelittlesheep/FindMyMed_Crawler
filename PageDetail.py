import Search_page_URL


def get_pageDetail(soup):
    page_content = []
    page_content.append(soup.find(id='medinfo-name').get_text(strip=True))  # 0

    # 1
    tags = soup.findAll(class_='new-tag label label-primary')
    tags_list = []
    for tags in tags:
        tags_list.append(tags.get_text(strip=True))
    page_content.append(tags_list)

    if soup.find(id='medinfo-cureitem_s-text') is None:  # 2
        page_content.append(soup.find(id='medinfo-cureitem-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-cureitem_s-text').get_text(strip=True))

    if soup.find(id='medinfo-aftereffect_s-text') is None:  # 3
        page_content.append(soup.find(id='medinfo-aftereffect-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-aftereffect_s-text').get_text(strip=True))

    if soup.find(id='medinfo-careitem_s-text') is None:  # 4
        page_content.append(soup.find(id='medinfo-careitem-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-careitem_s-text').get_text(strip=True))

    if soup.find(id='medinfo-contradictions_s-text') is None:  # 5
        page_content.append(soup.find(id='medinfo-contradictions-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-contradictions_s-text').get_text(strip=True))

    if soup.find(id='medinfo-mamiitem_s-text') is None:  # 6
        page_content.append(soup.find(id='medinfo-mamiitem-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-mamiitem_s-text').get_text(strip=True))

    if soup.find(id='medinfo-effect_s-text') is None:  # 7
        page_content.append(soup.find(id='medinfo-effect-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-effect_s-text').get_text(strip=True))

    if soup.find(id='medinfo-useway_s-text') is None:  # 8
        page_content.append(soup.find(id='medinfo-useway-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-useway_s-text').get_text(strip=True))

    if soup.find(id='medinfo-interaction_s-text') is None:  # 9
        page_content.append(soup.find(id='medinfo-interaction-text').get_text(strip=True))
    else:
        page_content.append(soup.find(id='medinfo-interaction_s-text').get_text(strip=True))

    return page_content

def get_sheet(soup):
    sheet = soup.find(id="sheet-zone")
    if sheet:
        return True

def text_process(soup):
    # 1
    tags_raw = get_pageDetail(soup)[1]
    tags_list = []
    for i in range(0, len(tags_raw)):
        tags_list.append(str(i+1) + '.' + tags_raw[i])
    # 5
    contradictions_raw = get_pageDetail(soup)[5]
    contradictions_list = contradictions_raw.split('。')
    # 6
    mamiitem_raw = get_pageDetail(soup)[6]
    mamiitem_list = mamiitem_raw.split('。')
    # 7
    effect_raw = get_pageDetail(soup)[7]
    effect_list = effect_raw.split('。')
    # 8
    useway_raw = get_pageDetail(soup)[8]
    useway_list = useway_raw.split('。')
    # 9
    interaction_raw = get_pageDetail(soup)[9]
    interaction_list = interaction_raw.split('。')


    return [tags_list, contradictions_list, mamiitem_list, effect_list, useway_list, interaction_list]

def main(input="Peritoneal"):
    if Search_page_URL.main(input) is True:
        return True
    else:
        drug_link = Search_page_URL.main(input)
        URL = drug_link
        soup = Search_page_URL.get_page(URL, str(None))
        if get_sheet(soup):
            return True
        else:
            return [get_pageDetail(soup), text_process(soup)]

    '''以下為印出葉面詳細資訊，作為檢查錯誤使用
    print("學名/藥名:" + '\n' + str(get_pageDetail(soup)[0]) + '\n')
    print("標籤:")
    for i in range(0, len(text_process(soup)[1])):
        print(text_process(soup)[1][i])
    print('')
    print("適應症:" + '\n' + str(get_pageDetail(soup)[2]) + '\n')
    print("副作用:" + '\n' + str(get_pageDetail(soup)[3]) + '\n')
    print("警語:" + '\n' + str(get_pageDetail(soup)[4]) + '\n')
    print("使用禁忌:")
    for i in range(0, len(text_process(soup)[1]) - 1):
        print(text_process(soup)[1][i] + '。')
    print('')
    print("懷孕/授乳注意事項:")
    for i in range(0, len(text_process(soup)[2]) - 1):
        print(text_process(soup)[2][i] + '。')
    print('')
    print("藥理作用:")
    for i in range(0, len(text_process(soup)[3]) - 1):
        print(text_process(soup)[3][i] + '。')
    print('')
    print("用法用量:")
    for i in range(0, len(text_process(soup)[4]) - 1):
        print(text_process(soup)[4][i] + '。')
    print('')
    print("交互作用:")
    for i in range(0, len(text_process(soup)[5]) - 1):
        print(text_process(soup)[5][i] + '。')
    print('')
    '''

if __name__ == '__main__':
    main()
