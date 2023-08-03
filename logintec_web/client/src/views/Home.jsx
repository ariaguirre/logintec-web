import React from 'react'
import { Link } from 'react-router-dom'
import styles from '../styles/home.module.css'


export function Home() {
    return (
      <div>
        <h1 className={styles.header}>Home page (cliente autorizado)</h1>
        <div className={styles.menus}>
          <Link to='/configuration'>
            <button className={styles.btn}>Configuración de sensores</button>
          </Link>
          <Link to='/operation'>
            <button className={styles.btn}>Operación</button>
          </Link>
          <Link to='/admin'>
            <button className={styles.btn}>Administración de usuarios</button>
          </Link>
        </div>
      </div>
    )
  }
  
  