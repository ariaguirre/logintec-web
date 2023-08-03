import React, {useState} from 'react'
import { Link } from 'react-router-dom'
import styles from '../styles/home.module.css'

export function Home() {
  const [opButtons, setOpButtons] = useState(false);
  
  const handleOpButtons = () => {
    setOpButtons(!opButtons);
  }

    return (
      <div>
        <h1 className={styles.header}>Home page (cliente autorizado)</h1>
        <div className={styles.menus}>
          <Link to='/configuration'>
            <button className={styles.btn}>Configuración de sensores</button>
          </Link>
          {/* <Link to='/operation'> */}
            <button className={styles.btn} onClick={handleOpButtons}>Operación</button>
            {opButtons && (
              <div>
                <button className={styles.opButtons}>Start measurment</button>
                <button className={styles.opButtons}>Stop measurment</button>
              </div>
            )}
          {/* </Link> */}
          <Link to='/admin'>
            <button className={styles.btn}>Administración de usuarios</button>
          </Link>
        </div>
      </div>
    )
  }
  
  