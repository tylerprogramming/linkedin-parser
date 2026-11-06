# Creating a LinkedIn Profile Parser

#### Things needed
[ ] - Tavily API: https://tavily.com/ \
[ ] - ScrapeDog API: https://www.scrapingdog.com/

#### Optional
[ ] - OpenAI API: can use **LM Studio** or **Ollama** for local LLM

#### Tech Stack
1. Flask
2. HTML/CSS
3. **AutoGen**
4. TavilyAPI - Web Scraping
5. ScrapeDogAPI - LinkedIn Scraping

#### Setup
Use Python 3.11 or 3.12: `pyautogen==0.2.24` requires Python below 3.13.

```bash
pip install -r requirements.txt
```

Put `TAVILY_API_KEY` and `SCRAPEDOG_API_KEY` in `.env`, and your OpenAI key in the `gpt-5.4-mini` entry of `OAI_CONFIG_LIST.json`. Then run `python app.py` and open http://127.0.0.1:5000/?input_data=<name>.

> **Model update:** this project originally used `gpt-3.5-turbo`, which OpenAI shut down on 2026-10-23 ([deprecations](https://developers.openai.com/api/docs/deprecations)). It now uses `gpt-5.4-mini`. To run locally instead, switch the `filter_dict` in `autogen_info/config.py` to the commented-out `phi2` (LM Studio) block.

Full YouTube Walkthrough: ***coming soon***