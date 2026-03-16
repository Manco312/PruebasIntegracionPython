
# Importa las implementaciones concretas usadas en esta prueba.
# Son parte del paquete "layers" que demuestra una separación clásica
# en repositorio-servicio-controlador (separation of concerns).
from layers.repository import InMemoryUserRepository
from layers.service import UserService
from layers.controller import UserController


def test_controller_service_repository_integration():
    """Prueba de integración de extremo a extremo para la arquitectura en capas.

    Esta prueba verifica que el controlador, el servicio y el repositorio
    colaboren correctamente para recuperar el nombre completo de un usuario.

    El repositorio es en memoria, el servicio
    contiene la lógica de negocio y el controlador expone la información.

    Las expectativas son:
      - el id de usuario 1 corresponde a "Ada Lovelace"
      - el id de usuario 2 corresponde a "Alan Turing"
      - un id de usuario desconocido devuelve un mensaje tipo 404
    """

    # Arrange: construir cada capa e inyectar dependencias.
    repo = InMemoryUserRepository()
    service = UserService(repo)
    controller = UserController(service)

    # Act + Assert: verificar la salida correcta para ids de usuario conocidos y desconocidos.
    assert controller.get_user_full_name(1) == "Ada Lovelace"
    assert controller.get_user_full_name(2) == "Alan Turing"
    assert controller.get_user_full_name(3) == "Grace Hopper"
    assert controller.get_user_full_name(999) == "404 NOT_FOUND"
