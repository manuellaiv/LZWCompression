import './App.css';
import React, {useState} from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [status, setStatus] = useState("Plain Text → Compressed Text");

  const handleChange = (e) => {
    setText(e.target.value);
  }

  const handleSubmit = () =>{
    if (status === "Plain Text → Compressed Text") {
      axios.post('http://localhost:8000/encode/', { text: text })
        .then(response => {
          console.log(response.data)
          setOutputText(response.data.encoded_result);
        })
        .catch(error => {
          setOutputText('');
          console.error(error);
        });
    }
    else{
      axios.post('http://localhost:8000/decode/', { text: text })
        .then(response => {
          console.log(response.data)
          setOutputText(response.data.decoded_result);
        })
        .catch(error => {
          console.error(error);
          setOutputText('');
        });
    }
  }

  function statusChange(){
    if (status === "Plain Text → Compressed Text"){
      setStatus("Compressed Text → Plain Text");
    }
    else{
      setStatus("Plain Text → Compressed Text");
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="title">LZW Compression</h1>
        <p className="status">{status}</p>
        <button class="reverse-button" onClick={statusChange}></button>

        <div className="input-grid">
          <textarea
          type="text"
          className="input-box"
          onChange={handleChange}
          style={{resize: 'none'}}
          />

          <textarea
          type="text"
          className="input-box"
          value={outputText}
          style={{resize: 'none'}}
          readOnly
          />
        </div>
        <p></p>
        <button class="submit-button" onClick={handleSubmit}></button>
      </header>
    </div>
  );
}

export default App;
