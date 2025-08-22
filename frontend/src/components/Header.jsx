import "./styles/Header.css";

export default function Header({ theme, setTheme }) {
  const toggle = () => setTheme(theme === "light" ? "dark" : "light");

  return (
    <header className="header">
      <div className="brand">
        <img src="/logo.png" alt="Logo" className="logo" />
        <div>
          <p>Find the right book with a friendly AI.</p>
        </div>
      </div>

      <button className="btn ghost theme-toggle" onClick={toggle}>
        {theme === "light" ? "🌙 Dark" : "☀️ Light"}
      </button>
    </header>
  );
}
