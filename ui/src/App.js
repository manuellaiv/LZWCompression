import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [status, setStatus] = useState("Plain Text → Compressed Text");

  const [data, setData] = useState([]);

  const handleChange = (e) => {
    setText(e.target.value);
  }

  const handleSubmit = () =>{
    if (status === "Plain Text → Compressed Text") {
      axios.post('http://localhost:8000/encode/', { text: text })
        .then(response => {
          console.log(response.data)
          fetchTable()
          setOutputText(response.data.encoded_result);
        })
        .catch(error => {
          fetchTable()
          setOutputText('Can not be encoded.');
          console.error(error);
        });
    }
    else{
      axios.post('http://localhost:8000/decode/', { text: text })
        .then(response => {
          console.log(response.data)
          fetchTable()
          setOutputText(response.data.decoded_result);
        })
        .catch(error => {
          console.error(error);
          fetchTable()
          setOutputText('Can not be decoded.');
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

  const fetchTable = () => {
    axios.get('http://localhost:8000/get-all-status/')
      .then(response => {
        const statusData = response.data.data;
        axios.get('http://localhost:8000/get-all-inp/')
          .then(response => {
            const inpData = response.data.data;
            axios.get('http://localhost:8000/get-all-out/')
              .then(response => {
                const outData = response.data.data;
                const dataArray = statusData.map((status, index) => {
                  let statusText = '';
                    if (status === 0) {
                      statusText = 'Plain Text → Compressed Text';
                    } else if (status === 1) {
                      statusText = 'Compressed Text → Plain Text';
                    }
                    return {
                      id: index + 1,
                      inp: inpData[index],
                      out: outData[index],
                      status: statusText
                    };
                });
                console.log(dataArray);
                setData(dataArray);
              })
              .catch(error => {
                console.error(error);
              });
          })
          .catch(error => {
            console.error(error);
          });
      })
      .catch(error => {
        console.error(error);
      });
  }

  useEffect(() => {
    fetchTable();
  }, []);

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

      <p className="status">History</p>

        <div className="table-container">
      <table>
        <thead>
          <tr>
            <th>Model</th>
            <th>Input</th>
            <th>Output</th>
          </tr>
        </thead>
        <tbody>
          {data.map(el => (
            <tr key={el.id}>
              <td>{el.status}</td>
              <td>{el.inp}</td>
              <td>{el.out}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
      </header>
    </div>
  );
}

export default App;
