import sqlite3
import nltk
#nltk.download()

def readFromSQL():

    conn = sqlite3.connect("/Users/tinlin/Box Sync/Project/GResults.db")
    c = conn.cursor()
    c.execute("select title,content from GResults where content  like '%redmart%' or title like '%redmart%'")
    rows = c.fetchall()
    conn.close()
    #testing
    return rows;
    print '-- fetch all -- (' + str(len(rows)) +")"


def extraction(corpus):
    # segmentation
    # tokenization
    # extraction

    return


if __name__ == '__main__':
    rows = readFromSQL();
    # title, content
    # name entity extraction: Organization, Location, Date
    for row in rows:
        title = row[0]
        content = row[1]
        print 'title:'
        print title
        sentences = nltk.sent_tokenize(content)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        for sent in sentences:
            print sent

    #testing

