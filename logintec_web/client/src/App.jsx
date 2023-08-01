import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import {Login} from './views/Login/';
import {Home} from './views/Home/';


function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Navigate to='login'/>} />
      <Route path='/login' element={<Login/>} />
      <Route path='/home' element={<Home/>} />
    </Routes>
    </BrowserRouter>
  )
}

export default App
