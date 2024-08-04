import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UserList from './components/UserList';
import InterestList from './components/InterestList';

function App() {
  return(
    <Router>
      <div className='App'>
        <Routes>
          <Route path='/users' Component={UserList} />
          <Route path='/interests' Component={InterestList} />
        </Routes>
      </div>
    </Router>
  );
}


export default App;