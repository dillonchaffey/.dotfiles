    r=do_gem(f'''
You are an expert python programmer. I have a bug in my code I would like you to help me fix.
I am running ubuntu. The error I am getting is:
{get_clipboard_text()}

The code that is giving me the error is:
{get_selected_text()}
    ''')
