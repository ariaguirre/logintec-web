import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import {Login} from './views/Login/';
import {Home} from './views/Home/';
import {Configuration} from './views/Configuration/';
import {Operation} from './views/Operation/';
import {Admin} from './views/Admin/';


function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Navigate to='login'/>} />
      <Route path='/login' element={<Login/>} />
      <Route path='/home' element={<Home/>} />
      <Route path='/configuration' element={<Configuration/>} />
      <Route path='/operation' element={<Operation/>} />
      <Route path='/admin' element={<Admin/>} />
    </Routes>
    </BrowserRouter>
  )
}

export default App
