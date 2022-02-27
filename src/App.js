import './App.css';
import './components/Waveform'
import Waveform from './components/Waveform';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Vocoder!
        </h1>
        <Waveform></Waveform>
        
      </header>
    </div>
  );
}

export default App;
