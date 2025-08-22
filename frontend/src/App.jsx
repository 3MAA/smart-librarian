import { useEffect, useState } from "react";
import { askAPI, ttsURL } from "./api";
import Header from "./components/Header";
import QueryForm from "./components/QueryForm";
import ResultCard from "./components/ResultCard";

export default function App() {
  const [theme, setTheme] = useState(() => localStorage.getItem("theme") || "light");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [answer, setAnswer] = useState(null);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  async function onAsk({ query, tts, voiceTrigger }) {
    setError("");
    setAnswer(null);
    const q = (query || "").trim();
    if (!q) {
      setError("Please enter a question.");
      return;
    }
    setLoading(true);
    try {
      const data = await askAPI(q, tts);
      if (data.filtered) {
        setError(data.recommendation || "Your message was filtered. Please rephrase.");
      } else {
        setAnswer(data);
        if (tts && data.tts_url) {
          setTimeout(() => {
            const audio = document.getElementById("smart-audio");
            if (audio) {
              audio.src = ttsURL(data.tts_url);
              audio.play().catch(() => {});
            }
          }, 220);
        }
      }
    } catch (e) {
      setError(e?.message || "Request failed");
    } finally {
      setLoading(false);
    }
  }

  return (
  <div className="page">
    <Header theme={theme} setTheme={setTheme} />

    <main className="container center-stage">
      <div className="stack">
        <QueryForm loading={loading} onAsk={onAsk} />
        {error && <div className="alert">{error}</div>}
        <ResultCard answer={answer} />
      </div>
    </main>

    <footer className="footer">
   
    </footer>
  </div>
);
}
