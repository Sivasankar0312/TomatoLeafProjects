from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

def translatetext():
    article_en="In the early stages of tomato leaf disease, preventive measures and prompt action are crucial. Begin by ensuring proper plant spacing for adequate air circulation and using well-draining soil. Water the plants at the base, avoiding foliage, to reduce humidity. Apply a layer of mulch to prevent soil-borne pathogens from splashing onto leaves. Regularly inspect plants for signs of disease, and promptly remove and destroy infected leaves. Utilize organic fungicides or neem oil as a preventive measure. Additionally, consider rotating crops yearly to minimize disease recurrence. Early intervention and a holistic approach contribute to effective management of tomato leaf diseases."
    model=MBartForConditionalGeneration.from_pretrained('facebook/mbart-large-50-many-to-many-mmt')
    tokenizer=MBart50TokenizerFast.from_pretrained('facebook/mbart-large-50-one-to-many-mmt',src_lang='en_XX')
    model_input=tokenizer(article_en,return_tensors="pt")
    gentok=model.generate(**model_input,forced_bos_token_id=tokenizer.lang_code_to_id['ta_IN'])
    translation=tokenizer.batch_decode(gentok,skip_special_tokens=True)
    return translation
