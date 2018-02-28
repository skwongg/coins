import React from 'react';
import PropTypes from 'prop-types';
import {Form, Button} from 'semantic-ui-react';
import isEmail from 'validator/lib/isEmail';
import InlineError from '../messages/InlineError'

class SignUpForm extends React.Component{
  state = {
    data: {
      email: '',
      password: '',
      passwordconf: '',
      username: '',
    },
    loading: false,
    errors: {}
  }

  onChange = e =>
    this.setState({
      ...this.state,
      data: {...this.state.data, [e.target.name]: e.target.value}
    });

  onSubmit = (e) => {
    e.preventDefault();
    const errors = this.validate(this.state.data);
    this.setState({errors});
    if (Object.keys(errors).length === 0) {
      this.setState({loading:true});
      this.props.submit(this.state.data)
        .catch(err => {
          debugger
          this.setState({errors:err.response.data.errors, loading: false})});
    }
  };

  validate = data => {
    const errors = {};
    if (!data.username) errors.username = "Username required";
    if (!data.first_name) errors.first_name = "First name required";
    if (!data.last_name) errors.last_name = "Last name required";
    if (!isEmail(data.email)) errors.email = "Invalid email";
    if (!data.password || (data.password !== data.passwordconf)) errors.password = "Password required";
    if (!data.passwordconf || (data.password !== data.passwordconf)) errors.passwordconf = "Please confirm your password";
    return errors;
  };

  render() {
    const { data, errors, loading} = this.state;

    return (
      <Form onSubmit={this.onSubmit} loading={loading}>

        <Form.Field error={!!errors.username}>
          <label htmlFor="username">username</label>
          <input type="text" id="username" name="username" placeholder="username" value={data.username} onChange={this.onChange}/>
          {errors.username && <InlineError text={errors.username}/>}
        </Form.Field>
        <Form.Field error={!!errors.first_name}>
          <label htmlFor="first_name">First Name</label>
          <input type="text" id="first_name" name="first_name" placeholder="first_name" value={data.first_name} onChange={this.onChange}/>
          {errors.first_name && <InlineError text={errors.first_name}/>}
        </Form.Field>
        <Form.Field error={!!errors.last_name}>
          <label htmlFor="last_name">Last Name</label>
          <input type="text" id="last_name" name="last_name" placeholder="last_name" value={data.last_name} onChange={this.onChange}/>
          {errors.last_name && <InlineError text={errors.last_name}/>}
        </Form.Field>


        <Form.Field error={!!errors.email}>
          <label htmlFor="email">Email</label>
          <input type="email" id="email" name="email" placeholder="email@email.com" value={data.email} onChange={this.onChange}/>
          {errors.email && <InlineError text={errors.email}/>}
        </Form.Field>

        <Form.Field error={!!errors.password}>
          <label htmlFor="password">Password</label>
          <input type="password" id="password" placeholder="DogecoinBestCoin!@#$1234"  name="password" value={data.password} onChange={this.onChange}/>
          {errors.password && <InlineError text={errors.password}/>}
        </Form.Field>

        <Form.Field error={!!errors.passwordconf}>
          <label htmlFor="passwordconf">Password Confirmation</label>
          <input type="password" id="passwordconf" placeholder="DogecoinBestCoin!@#$1234" name="passwordconf" value={data.passwordconf} onChange={this.onChange}/>
          {errors.passwordconf && <InlineError text={errors.passwordconf}/>}
        </Form.Field>

        <Button primary>Sign Up</Button>
      </Form>
    );
  }
}

SignUpForm.propTypes = {
  submit:PropTypes.func.isRequired
};

export default SignUpForm;
