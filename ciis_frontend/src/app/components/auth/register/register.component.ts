import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../../services/auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  registerForm: FormGroup;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  onSubmit(): void {
    if (this.registerForm.valid) {
      const { email, password } = this.registerForm.value;
      this.authService.register({ email, password }).subscribe({
        next: () => {
          // Si el registro es exitoso, lo enviamos a la página de documentos
          this.router.navigate(['/documentos']);
        },
        error: (err) => {
          // Manejo de errores comunes de Firebase
          if (err.code === 'auth/email-already-in-use') {
            this.errorMessage = 'Este correo electrónico ya está en uso.';
          } else {
            this.errorMessage = 'Ocurrió un error durante el registro.';
          }
          console.error(err);
        }
      });
    }
  }
}
