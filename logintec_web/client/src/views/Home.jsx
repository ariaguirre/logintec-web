import styles from '../styles/home.module.css'

export function Home() {
    return (
      <div>
        <h1 className={styles.header}>Home page</h1>
        <div className={styles.menus}>
            <button className={styles.btn}>Configuración de sensores</button>
            <button className={styles.btn}>Operación</button>
        </div>
      </div>
    )
  }
  
  