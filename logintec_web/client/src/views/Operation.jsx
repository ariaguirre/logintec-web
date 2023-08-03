import React from 'react'
import styles from '../styles/operation.module.css'

export function Operation() {
  return (
    <div>
      <h1 className={styles.header}>Operación de sensores</h1>
      <h2>Información sobre configuración de los sensores.</h2>
      <button className={styles.btn}>Start measurment</button>
      <button className={styles.btn}>Stop measurment</button>
    </div>
  )
}
