import gdata.docs.service
def google_query() :
    

    # Create a client class which will make HTTP requests with Google Docs server.
    client = gdata.docs.service.DocsService()
    # Authenticate using your Google Docs email address and password.
    client.ClientLogin('mahi.access06@gmail.com', 'Mahima23@@') 
    # Query the server for an Atom feed containing a list of your documents.
    documents_feed = client.GetDocumentListFeed()
    # Loop through the feed and extract each document entry.
    for document_entry in documents_feed.entry:
        # Display the title of the document on the command line.
        print(document_entry.title.text)

