import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import styles from '../styles/login.module.css/'

export function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    }
    
    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
    }

  return (
    <div className={styles.container}>
        <h1 className={styles.header}>Ingrese a su cuenta</h1>
        <br/>
        <form className={styles.form}>
        <select>
            <option>Cliente autorizado</option>
            <option>Mantenimiento</option>
            <option>Servicio</option>
        </select>
            <div>
                    <input
                    type='password'
                    id='password'
                    placeholder="Contraseña"
                    value={password}
                    onChange={handlePasswordChange}
                    required
                    />
            </div>
            <Link to="/home">
            <button className={styles.btn}>Iniciar sesión</button>
            </Link>
        </form>

    </div>
  )
}

