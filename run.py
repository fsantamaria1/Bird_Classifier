from streamlit.web import bootstrap

# Used to run the streamlit code locally

real_script = 'main.py'
bootstrap.run(real_script, f'run.py {real_script}', [], {})