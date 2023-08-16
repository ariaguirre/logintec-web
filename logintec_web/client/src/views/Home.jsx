import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from '../styles/home.module.css';

export function Home() {
  const [opButtons, setOpButtons] = useState(false);
  const [configBtn, setConfigBtn] = useState(false);

  const handleOpButtons = () => {
    if(configBtn==true) setConfigBtn(false);
    setOpButtons(!opButtons);
  };

  const handleConfigBtn = () => {
    if(opButtons==true) setOpButtons(false);
    setConfigBtn(!configBtn);
  };

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
          {/* <Link to='/admin'>
            <button className={styles.btn}>Administración de usuarios</button>
          </Link> */}
        </div>
      </div>
      <div className={styles.allCont}>
        {opButtons && (
          <div className={styles.opCont}>
            <div>
              <h2>Configuración actual</h2>
              <label>Frecuencia / Ángulo  XXXX</label>
              <h3>LMS time</h3>
                  <div className={styles.formGroup}>
                  <label>Fecha del dispositivo:  XXXX</label>
                  <label>Hora del dispositivo:   XXXX</label>
                  </div>
                  <br/>
                  <h3>Rango de ángulos</h3>
                  <div className={styles.formGroup}>
                    <div className={styles.angleInput}>
                      <label>Ángulo inicial  XXXX  </label>
                    </div>
                    <div className={styles.angleInput}>
                      <label>Ángulo final  XXXX  </label>
                    </div>
                    </div>
            </div>
            <div className={styles.btnCont}>
            <button className={styles.opButtons}>Conectar</button>
            <button className={styles.opButtons}>Stand by</button>
            <button className={styles.opButtons}>Start measurment</button>
            <button className={styles.opButtons}>Stop measurment</button>
            </div>
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
                    <option>25Hz / 0.25°</option>
                    <option>35Hz / 0.25°</option>
                    <option>35Hz / 0.5°</option>
                    <option>50Hz / 0.3333°</option>
                    <option>50Hz / 0.5°</option>
                    <option>75Hz / 0.5°</option>
                    <option>75Hz / 1°</option>
                    <option>100Hz / 0.6667°</option>
                    <option>100Hz / 1°</option>
                    <option>50Hz / 0.1667° interlaced</option>
                    <option>75Hz / 0.25° interlaced</option>
                    <option>100Hz / 0.1667° interlaced</option>
                    <option>100Hz / 0.3333° interlaced</option>
                    <option>100Hz / 0.5° interlaced</option>
                    <option>25Hz / 0.083° interlaced</option>
                    <option>25Hz / 0.042° interlaced</option>
                  </select>
                  </div>
                  <br/>
                  <h3>LMS time</h3>
                  <div className={styles.formGroup}>
                  <div className={styles.angleInput}>
                  <label>Fecha del dispositivo:</label>
                  <input type='text'/>
                  </div>
                  <div className={styles.angleInput}>
                  <label>Hora del dispositivo:</label>
                  <input type='text'/>
                  </div>
                  </div>
                  <button className={styles.boton}>Actualizar</button>
                  <br/>
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
                    <button className={styles.actBoton}>Actualizar configuración</button>
                </form>
              )}
          </div>
            </div>
      </div>
    )
  }
  
  