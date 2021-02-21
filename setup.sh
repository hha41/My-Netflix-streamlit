mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"jsa48@mail.aub.edu\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml