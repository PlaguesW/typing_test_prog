import { useEffect, useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [input, setInput] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:8000/text/random')
      .then(res => res.json())
      .then(data => {
        setText(data.text || 'failed to load');
      });
  }, []);

  return (
    <div style={{ padding: 40, fontFamily: 'monospace', fontSize: 20 }}>
      <div style={{ marginBottom: 20 }}>{text}</div>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        style={{ width: '100%', padding: 10, fontSize: 18 }}
      />
    </div>
  );
}

export default App;