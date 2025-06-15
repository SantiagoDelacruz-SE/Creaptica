import { Routes } from '@angular/router';
import { InicioComponent } from './components/inicio/inicio.component';
import { ListaDocumentosComponent } from './components/lista-documentos/lista-documentos.component';
import { LoginComponent } from './components/auth/login/login.component';
import { RegisterComponent } from './components/auth/register/register.component';

export const routes: Routes = [
    { path: 'inicio', component: InicioComponent },
    { path: 'documentos', component: ListaDocumentosComponent },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: '', redirectTo: '/inicio', pathMatch: 'full' }
];
