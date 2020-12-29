import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';

import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { RegisterComponent } from './register/register.component';
import { LoginRedirectService } from './services/Auth/login-redirect.service';
import { EnsureAuthenticatedService } from './services/Auth/ensure-authenticated.service';

export const AppRoutes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
    // canActivate: [EnsureAuthenticatedService]
  },
  {
    path: '',
    component: AdminLayoutComponent,
    children: [
        {
      path: '',
      loadChildren: './layouts/admin-layout/admin-layout.module#AdminLayoutModule'
      }],
     canActivate: [EnsureAuthenticatedService]
  },
  {
    path: 'sandbox',
    component: RegisterComponent,
    pathMatch: 'full',
  },
  {
    path: 'login',
    component: LoginComponent,
    canActivate: [LoginRedirectService]
  },
  {
    path: 'register',
    component: RegisterComponent,
    canActivate: [LoginRedirectService]
  },
  {
    path: 'dashboard',
    redirectTo: 'dashboard',
    canActivate: [EnsureAuthenticatedService]
  }
]
