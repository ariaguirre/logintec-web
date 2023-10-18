import React, { useState } from 'react';
import styles from '../styles/home.module.css';
import axios from 'axios';

export function Home() {
  const [opButtons, setOpButtons] = useState(false);
  const [configBtn, setConfigBtn] = useState(false);
  const [status, setStatus] = useState('');
  const [start, setStart] = useState('');
  const [time, setTime] = useState('');
  const [date, setDate] = useState('');
  const [scan, setScan] = useState('');
  const [angle, setAngle] = useState('');
  const[sensorHeight, setSensorHeight] = useState(840);
  const [graph, setGraph] = useState('');
  // const [showText, setShowText] = useState(true);


  const handleOpButtons = () => {
    if(configBtn==true) setConfigBtn(false);
    setOpButtons(!opButtons);
  };

  const handleConfigBtn = () => {
    if(opButtons==true) setOpButtons(false);
    setConfigBtn(!configBtn);
  };

  const handleConnect = async () => {
    try{
      const response = await axios.get('http://127.0.0.1:8000/connect/');
      const message = response.data.message;
      alert(message)
    } catch(error) {
      console.log('Error connecting:', error)
      alert(message)
    }
  };

  const handleStatus = async (event) => {
    try{
      event.preventDefault();
      const response = await axios.get('http://127.0.0.1:8000/standby/');
      setStatus(response.data);
      const time = response.data.split("Hora: ")[1].split(" -")[0];
      setTime(time)
      const date = response.data.split("Fecha: ")[1];
      setDate(date)
    } catch(error){
      console.log('Error:', error);
      setStatus(response.data);
    }
  }

  const handleStart = async () => {
    try{
      const response = await axios.get('http://127.0.0.1:8000/start/');
      setStart(response.data.message);
    } catch (error){
      console.log('Error:', error)
      setStart(response.data.message)
    }
  }

  const handleScan = async () => {
    try{
      const response = await axios.get(`http://127.0.0.1:8000/scandata/?height=${sensorHeight}`);
      // console.log(response.data)
      const arr = response.data.split(" ");
      const penultimateHex = arr[arr.length - 2];
      const angle = (parseInt(penultimateHex, 16)/10000); 
      setAngle(angle)
      setScan(response.data)
    } catch(error){
      console.log('Error scanning: ', error);
      setScan(response.data);
    }
  }

  const handleSensor = async(event) =>{
    event.preventDefault();
    setSensorHeight(event.target.value)
  }

  const handleGraphic = async () => {
    try{
      const list = await axios.get(`http://127.0.0.1:8000/list/?height=${parseFloat(sensorHeight)}`);
      console.log('sensorHeight FRONT',sensorHeight)
      const cleaned = await axios.get(`http://127.0.0.1:8000/clean/?height=${parseFloat(sensorHeight)}`);
      const graph = cleaned.data;
      // setGraph(graph)
      // console.log(graph)
    } catch(error){
      console.log('Error handling graphic:', error);
    }
  }

  // const handleClean = () => {
  //   setShowText(false);
  // };

  return (
    <div>
      <h1 className={styles.header}>Home page (cliente autorizado)</h1>
      <div className={styles.container}>
        <div className={styles.menus}>
          <button className={`${styles.btn} ${configBtn ? styles.activeButton : ''}`} onClick={handleConfigBtn}>
            Configuración de sensores
          </button>
          <button className={`${styles.btn} ${opButtons ? styles.activeButton : ''}`} onClick={handleOpButtons}>
            Operación
          </button>
        </div>
      </div>
      <div className={styles.allCont}>
        {opButtons && (
          <div className={styles.opCont}>
            <div>
              <h2>Configuración actual</h2>
              <label>Frecuencia / Resolución: 25Hz / 0.1667°</label>
              <br/>
              <br/>
              <label>Altura del sensor: </label> 
              {sensorHeight}
              <h3>LMS time</h3>
              <p>Fecha del dispositivo: {date}</p>
              <p>Hora del dispositivo: {time}</p>
              <h3>Rango de ángulos</h3>
              <div className={styles.angleInput}>
                <label>Ángulo inicial  {angle}°  </label>
              </div>
              <div className={styles.angleInput}>
                <label>Ángulo final  85°  </label>
              </div>
            </div>
            <div className={styles.btnCont}>
              <button className={styles.opButtons} onClick={handleConnect}>Conectar</button>
              <button className={styles.opButtons} onClick={handleStatus}>Stand by</button>
              <button className={styles.opButtons} onClick={handleStart}>Start measurment</button>
              <button className={styles.opButtons} onClick={handleScan}>Scan</button>
              <button className={styles.opButtons} onClick={handleGraphic}>Graph</button>
              {/* <button className={styles.opButtons} onClick={handleClean}>Clean</button> */}
              <div>
                {/* <img src={`http://127.0.0.1:8000/${graphImageUrl}`} alt="Gráfico" /> */}
              </div>
            </div>
            {/* {showText && ( */}
              <div>
                {status}
                <br />
                {start}
                <br />
                {scan}
              </div>
            {/* )} */}
          </div>
        )}
        <div className={styles.config}>
          {configBtn && (
            <form>
              <h2>Configuración del sensor</h2>
              <div className={styles.angleInput}>
                <label>Frecuencia / Ángulo</label>
                <select>
                  <option>25Hz / 0.1667°</option>
                  {/* ... (other options) */}
                </select>
                <br />
                <label>Altura del sensor</label>
                <input type='number' value={sensorHeight} onChange={handleSensor} />
              </div>
              <br />
              <h3>LMS time</h3>
              <div className={styles.angleInput}>
                <label>Fecha del dispositivo: {date}</label>
              </div>
              <div className={styles.angleInput}>
                <label>Hora del dispositivo: {time}</label>
              </div>
              <br />
              <button className={styles.boton} onClick={handleStatus}>Actualizar</button>
              <br />
              <h3>Rango de ángulos</h3>
              <div className={styles.formGroup}>
                <div className={styles.angleInput}>
                  <label>Ángulo inicial</label>
                  <input type='text' />
                </div>
                <div className={styles.angleInput}>
                  <label>Ángulo final</label>
                  <input type='text' />
                </div>
              </div>
              {/* <button className={styles.actBoton}>Actualizar configuración</button> */}
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
  