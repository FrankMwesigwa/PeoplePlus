import React, { Component } from 'react';
import axios from 'axios';

class EditDepartments extends Component {

  state = {
      branch: {}
}

  componentDidMount = () => {
    const id = this.props.match.params.id
    axios.get('http://127.0.0.1:5000/department/'+id)
    .then(response => {
      this.setState({ department: response.data });
      console.log(this.state.branch);
    });
  }

  handleChange = (e) => {
    const state = this.state.department
    state[e.target.name] = e.target.value;
    this.setState({department:state});
  }

  handleSubmit = (e) => {
    e.preventDefault();
    const id = this.props.match.params.id
    const { departmentname, departmentlocation } = this.state.department;

    axios.put('http://127.0.0.1:5000/department/'+id, { departmentname, departmentlocation })
      .then(result => {
        console.log(result.data)
        this.props.history.push('/department/'+id)
      });
  }

  render() {
    return (
        <div>

            
        <div class="box box-warning">
          
          <div class="box-body">
          <form className="white" onSubmit={this.handleSubmit}>
          <div class="form-group">
            <label>Department departmentname</label>
            <input type="text" class="form-control" name="name" value ={this.state.department.departmentname} onChange={this.handleChange} placeholder="Enter Departement Name"/>
          </div>

          <div class="form-group">
            <label>Department DepartmentLocation</label>
            <input type="text" class="form-control" name="location" value ={this.state.branch.location} onChange={this.handleChange} placeholder="Enter department Location"/>
          </div>

          <div class="footer">
              <button type="submit" className="btn btn-success">Edit Department</button>
        </div>

          </form>
          </div>
        </div>

</div>
    );
  }
}

export default EditDepartments;