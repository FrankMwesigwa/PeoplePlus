import React, {Component} from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

class CreateDepartment extends Component {

  state = {
      departments: []
  }

  componentDidMount = () => {
    axios.get('http://127.0.0.1:5000/departments')
      .then(response => {
        this.setState({ departments: response.data });
      })
      .catch(error => {
        console.log(error);
    })
  }

  render() {
    return (
      <div>

  <section class="content container-fluid">
  <div class="row">
    <div class="col-xs-12">
    <div class="box box-default">
            <div class="box-header with-border">
              <h3 class="box-title">Branch List</h3>
            </div>
            <div class="box-body">
              <button type="button" class="btn btn-primary">
                <Link to="/department/add"> Add Department</Link>
              </button>
            </div>

            <div class="box-body">

            <table id="example1" class="table table-bordered table-striped">
                <thead>
                <tr>
                  <th>Department Id</th>
                  <th>Department Name</th>
                  <th>Department Location</th>
                </tr>
                </thead>
                <tbody>
                      {
                        this.state.departments.map(branch => (
                        <tr key={department.id}>
                          <td>{department.id}</td>
                          <td>{department.name}</td>
                          <td>{department.location}</td>
                          <td><Link to={'/departments/${department.id}'}>Department Details</Link></td>
                        </tr>
                        ))
                      }                      
                    </tbody>             
              </table>
            
            </div>

          </div>

          </div>
           
      </div>

  </section>
</div>
    )
  }
}


export default CreateDepartment;