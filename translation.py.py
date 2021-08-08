from deep_translator import GoogleTranslator
import pandas as pd

#https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5


def trans_shops():
    df_shops = pd.read_csv("data/shops.csv",encoding="utf-8")
    trans = []
    for to_translate in df_shops['shop_name'].to_list():
        translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
        trans.append(translated)
        print(translated)
    df_shops['new'] = trans
    df_shops.to_csv('shops_en.csv',index=False)

def trans_item_cat():
    df_item_cat = pd.read_csv("data/item_categories.csv",encoding="utf-8")
    trans = []
    for to_translate in df_item_cat['item_category_name'].to_list():
        translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
        trans.append(translated)
        print(translated)
    df_item_cat['new'] = trans
    df_item_cat.to_csv('item_cat_en.csv',index=False)

def trans_items():
    df_item = pd.read_csv("data/items.csv",encoding="utf-8")
    trans = []
    fail = []
    count = 0
    for to_translate in df_item['item_name'].to_list():
        count +=1
        try:
            translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
            print(count,':',translated)
            trans.append(translated)
        except:
            trans.append(to_translate)
            fail.append(to_translate)


    df_item['new'] = trans
    df_item.to_csv('item_en.csv',index=False)
    print(fail)
    print(len(fail))


trans_shops()