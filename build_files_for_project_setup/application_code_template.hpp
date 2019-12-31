#pragma once
#include "../../component_framework/components/Component.hpp"
#include "../../freertos_distro/FreeRTOS_tasks/Application_interfaces.hpp"

class Application_code : public I_application_code, public Component {
public:
    Application_code(const char* name, const char * id);
    virtual ~Application_code(){};
    void Update();
};