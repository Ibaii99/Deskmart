import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthorizationService } from 'app/services/Auth/authorization.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html'
})
export class RegisterComponent implements OnInit {

  formGroup: FormGroup;

  constructor(private fb: FormBuilder, private backend: AuthorizationService, private router:Router) {
    this.formGroup = fb.group({
      username: new FormControl('', Validators.required),
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
      confirm_password: new FormControl('', Validators.required),
      first_name: new FormControl('', Validators.required),
      last_name: new FormControl('', Validators.required),
      address: new FormControl(''),
      city: new FormControl(''),
      country: new FormControl(''),
      postal_code: new FormControl(''),
      about: new FormControl('')
    }, {validator: this.samePasswor}
    );
   }

  ngOnInit(): void {
  }


  onRegister() {
    console.log(this.formGroup.getRawValue());
    this.backend.register(this.formGroup.getRawValue()).then(
      (user) => {
        console.log(user);
        localStorage.setItem('token', user.Authorization);
        if (localStorage.token) {
          this.router.navigate(['/dashboard']);
          console.log(localStorage.token);
        }
        else {
        }
      }
    );

  }

  login() {
    this.router.navigate(['login']);
  }

  samePasswor(formGroup: FormGroup) {
    return formGroup.get('password').value === formGroup.get('confirm_password').value ? null : { notSame: true }
  }

}
