import React, { Component } from 'react';
import { BrowserRouter, Route , Switch } from 'react-router-dom';

import Header from './components/layout/header'
import Dashboard from './components/layout/dashboard'

import AddDepartment from './components/departments/addDepartment'
import CreateDepartment from '.components/departments/createDepartment'
import ViewDepartment from './components/departments/detailsDepartment'
import EditDepartment from './components/departments/editDepartment'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <div className="container">
        <Header/>
        <Switch>
          <Route exact path='/' component={Dashboard} />
          <Route exact path='/department/add' component={AddDepartment} />
          <Route exact path='/departments' component={CreateDepartment} />
          <Route exact path='/department/:id' component={ViewDepartment} />
          <Route exact path='/departmentedit/:id' component={EditDepartment />
        </Switch>

      </div>
      </BrowserRouter>
    );
  }
  }

export default ;
