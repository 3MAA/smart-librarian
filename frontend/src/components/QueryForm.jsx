import "./styles/QueryForm.css";

import { useEffect, useMemo, useState } from "react";

export default function QueryForm({ loading, onAsk }) {
  const [query, setQuery] = useState("");
  const [tts, setTts] = useState(false);
  const [voiceMode, setVoiceMode] = useState(false);

  const speechSupported = useMemo(
    () => "webkitSpeechRecognition" in window || "SpeechRecognition" in window,
    []
  );

  useEffect(() => {
    if (!voiceMode) return;
    if (!speechSupported) {
      setVoiceMode(false);
      return;
    }
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    const rec = new SR();
    rec.lang = "en-US";
    rec.interimResults = false;
    rec.maxAlternatives = 1;

    rec.onresult = (ev) => {
      const text = ev.results[0][0].transcript;
      setQuery(text);
      setVoiceMode(false);
      onAsk({ query: text, tts, voiceTrigger: true });
    };
    rec.onerror = () => setVoiceMode(false);
    rec.start();
    return () => {
      try { rec.stop(); } catch {}
    };
  }, [voiceMode]); 

  function submit(e) {
    e.preventDefault();
    onAsk({ query, tts });
  }

  return (
    <form className="card" onSubmit={submit}>
      <label className="label">Ask for a recommendation</label>
      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        rows={3}
        placeholder="e.g., I’d like a book about the American Dream."
        className="textarea"
      />
      <div className="row">
        <label className="check">
          <input
            type="checkbox"
            checked={tts}
            onChange={(e) => setTts(e.target.checked)}
          />
          <span>Generate audio</span>
        </label>

        <div className="actions">
          <button
            type="button"
            className="btn secondary"
            onClick={() => setVoiceMode(true)}
            disabled={!speechSupported || loading}
            title={!speechSupported ? "Voice not supported" : "Speak your query"}
          >
            🎤 Voice
          </button>
          <button className="btn primary" type="submit" disabled={loading}>
            {loading ? "Thinking…" : "Ask"}
          </button>
        </div>
      </div>
    </form>
  );
}
