const BASE_URL = 'http://localhost:8000';

export async function askAPI(query, tts = false) {
  const res = await fetch(`${BASE_URL}/ask`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, tts }),
  });
  if (!res.ok) {
    let msg = '';
    try { msg = (await res.json())?.detail || (await res.text()); }
    catch { msg = await res.text(); }
    throw new Error(msg || 'Request failed');
  }
  return res.json();
}

export function ttsURL(rel) {
  return `${BASE_URL}${rel}`;
}
