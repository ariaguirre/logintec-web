import React from 'react';
import styles from '../styles/admin.module.css'

export function Admin() {
  return (
    <div>
      <h1 className={styles.header}>Administración de usuarios</h1>
      <h3>Lista de usuarios, posibilidad de modificar sus permisos, contraseñas, emails.</h3>
    </div>
  )
}
