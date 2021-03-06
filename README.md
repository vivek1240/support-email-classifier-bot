# support-email-classifier-bot
This project is a part of my work as a data science intern at **Yatra.com**

There are nearly **500 emails** fired each day to **yatra’s support team** from customers with various queries.

The support team **manually resolves** these queries and labels them with the following categories, cancellation, Refund, Booking Information, Eticket/Voucher, Promotions, Website Error, Amendments, etc., accordingly.

This project **resolves manual labeling** using a **multi-class text classifier** to classify text to a suitable category accurately.

The **BeautifulSoup** and **Unescape** are used to **clean** the raw email body. The basic **preprocessing** is done using **NLTK**(tokenization), **gensim**(simple preprocess and stop words removal), **Spacy**(lemmatization).
The **TF-IDF vectorizer** is used to **vectorize the text** data followed by **Chi2** for 1000 **optimal feature selection** and then applied the **classification algorithms**. Deployed the model using **Flask**. 

For Indepth understanding refer my article published https://vwake2017iitkgp.medium.com/multiclass-email-classification-from-scratch-4bc0f0c6c64d

**Steps to use the API:**

Steps to build:
1. Build docker->sudo docker build -t classifier .
2. Start docker->sudo docker run -p 9999:9999 classifier

**Code to hit the API:**

    import requests
    import json
    query = {
        "sent": 'I have made a flight booking on Yatra. My PNR No are S6ZF2Y . I had booked a return flight for both the PNR. The outbound flight i.eรย "BOM -          TRV"รย had been cancelled by the airways and the full amount has been credited back to my account.รย Now the Inbound flight i.e."รย TRV -รย BOM " has also      been cancelled by the airways and the full amount has been processed to the yatra account on 24th Feb 2020. So I want you to refund me the amount ASAP. When        would I get the refund back?Waiting for your reply'
    }

    requests.post("http://0.0.0.0:9999/classify", data= json.dumps(query)).json()
