from llm.schemas import Command

def route_intent(text: str) -> Command:
    t = text.lower()
    if "open " in t and ("chrome" in t or "browser" in t):
        return Command(
            intent="open_browser",
            normalized_text=text,
            tool="open_app",
            params={"app_name": "chrome"},
            confidence=0.9
        )
    if "create" in t and "folder" in t:
        return Command(
            intent="create_folder",
            normalized_text=text,
            tool="create_folder",
            params={"path": "Desktop/UltronFolder"},
            confidence=0.8
        )
    if "search" in t or "google" in t:
        # very rough extraction
        query = text.split("search", 1)[-1].replace("google", "").strip()
        return Command(
            intent="search_web",
            normalized_text=text,
            tool="search_web",
            params={"query": query or "HoloMat projector camera"},
            confidence=0.7
        )
    return Command(
        intent="generic",
        normalized_text=text,
        tool=None,
        params={},
        confidence=0.5
    )
