import { useEffect, useRef, useState } from "react";
import { ttsURL } from "../api";
import "./styles/ResultCard.css";

export default function ResultCard({ answer }) {
  if (!answer) return null;

  const { title, recommendation, full_summary, tts_url } = answer;

  const audioRef = useRef(null);
  const menuRef = useRef(null);

  const [open, setOpen] = useState(false);
  const [volume, setVolume] = useState(1);
  const [speed, setSpeed] = useState(1);

  useEffect(() => {
    if (!tts_url || !audioRef.current) return;
    const url = ttsURL(tts_url);
    const a = audioRef.current;
    a.src = url;
    a.volume = volume;
    a.playbackRate = speed;
    a.play().catch(() => { });
  }, [tts_url]);

  useEffect(() => {
    function onDocClick(e) {
      if (!open) return;
      if (!menuRef.current) return;
      if (!menuRef.current.contains(e.target)) setOpen(false);
    }
    function onEsc(e) {
      if (e.key === "Escape") setOpen(false);
    }
    document.addEventListener("mousedown", onDocClick);
    document.addEventListener("keydown", onEsc);
    return () => {
      document.removeEventListener("mousedown", onDocClick);
      document.removeEventListener("keydown", onEsc);
    };
  }, [open]);

  function onVolumeChange(e) {
    const v = Number(e.target.value);
    setVolume(v);
    if (audioRef.current) audioRef.current.volume = v;
  }
  function onSpeedChange(e) {
    const r = Number(e.target.value);
    setSpeed(r);
    if (audioRef.current) audioRef.current.playbackRate = r;
  }

  return (
    <section className="card result">
      {title && !answer.filtered && (
        <div className="result-header">
          <div className="badge">Recommendation</div>
          <h2 className="title">{title}</h2>
        </div>
      )}
      {recommendation && !answer.filtered && (
        <div className="block">
          <div className="eyebrow">Why this book</div>
          <p className="text">{recommendation}</p>
        </div>
      )}

      {full_summary && (
        <div className="block">
          <div className="eyebrow">Full summary</div>
          <p className="text pre">{full_summary}</p>
        </div>
      )}

      {tts_url && (
        <div className="block">
          <div className="audio-wrap">
            <audio ref={audioRef} className="audio" controls preload="none" />

            <button
              type="button"
              className="audio-kebab"
              aria-haspopup="true"
              aria-expanded={open}
              title="Audio options"
              onClick={() => setOpen(o => !o)}
            >
              <span className="dots">⋯</span>
            </button>

            {open && (
              <div className="audio-menu" ref={menuRef} role="menu">
                <div className="menu-row">
                  <span>Volume</span>
                  <input
                    type="range"
                    min="0" max="1" step="0.01"
                    value={volume}
                    onChange={onVolumeChange}
                  />
                  <span className="val">{Math.round(volume * 100)}%</span>
                </div>

                <div className="menu-row">
                  <span>Speed</span>
                  <select value={speed} onChange={onSpeedChange}>
                    <option value="0.75">0.75</option>
                    <option value="1">1 (Normal)</option>
                    <option value="1.25">1.25</option>
                    <option value="1.5">1.5</option>
                    <option value="1.75">1.75</option>
                    <option value="2">2</option>
                  </select>
                </div>

                <div className="menu-row">
                  <a
                    className="menu-download"
                    href={`${ttsURL(tts_url)}&download=1`}
                    download
                    onClick={() => setOpen(false)}
                  >
                    Download
                  </a>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </section>
  );
}
