sor1 = [0.028, 0.064, 0.088, 0.052, 0.076, 0.116, 0.060, 0.076, 0.088, 0.104, 0.084, 0.088, 0.052, 0.088, 0.048, 0.084, 0.076, 0.080, 0.092, 0.068, 0.116, 0.104, 0.052, 0.092, 0.096, 0.116, 0.084, 0.096, 0.096, 0.064, 0.072, 0.056, 0.108, 0.032, 0.112, 0.072, 0.072, 0.088, 0.124, 0.072, 0.076, 0.080, 0.092, 0.076, 0.052, 0.076, 0.064, 0.096, 0.080, 0.084, 0.048, 0.088, 0.096, 0.132, 0.096, 0.056, 0.080, 0.036, 0.080, 0.060, 0.104, 0.124, 0.060, 0.092, 0.104, 0.104, 0.064, 0.084, 0.064, 0.100, 0.072, 0.076, 0.140, 0.124, 0.060, 0.088, 0.060, 0.072, 0.092, 0.120, 0.092, 0.092, 0.036, 0.060, 0.064, 0.120, 0.088, 0.052, 0.064, 0.088, 0.124, 0.076, 0.012, 0.076, 0.088, 0.064, 0.080, 0.056, 0.116, 0.080]
sor2 = [0.164, 0.204, 0.164, 0.196, 0.168, 0.216, 0.216, 0.176, 0.200, 0.248, 0.176, 0.192, 0.196, 0.212, 0.188, 0.200, 0.208, 0.180, 0.204, 0.156, 0.208, 0.220, 0.204, 0.168, 0.192, 0.212, 0.164, 0.232, 0.208, 0.148, 0.180, 0.192, 0.152, 0.160, 0.144, 0.272, 0.160, 0.224, 0.220, 0.180, 0.164, 0.268, 0.188, 0.224, 0.176, 0.144, 0.164, 0.240, 0.168, 0.188, 0.156, 0.160, 0.184, 0.188, 0.180, 0.164, 0.196, 0.204, 0.140, 0.172, 0.220, 0.156, 0.192, 0.172, 0.256, 0.208, 0.132, 0.192, 0.236, 0.184, 0.188, 0.200, 0.220, 0.148, 0.232, 0.248, 0.224, 0.164, 0.252, 0.240, 0.204, 0.216, 0.152, 0.216, 0.192, 0.180, 0.148, 0.188, 0.156, 0.212, 0.212, 0.172, 0.144, 0.188, 0.216, 0.220, 0.212, 0.164, 0.228, 0.220]
sor3 = [0.264, 0.244, 0.260, 0.264, 0.248, 0.264, 0.252, 0.276, 0.256, 0.256, 0.248, 0.240, 0.236, 0.252, 0.272, 0.244, 0.220, 0.272, 0.264, 0.272, 0.232, 0.236, 0.264, 0.260, 0.276, 0.272, 0.280, 0.244, 0.256, 0.252, 0.268, 0.256, 0.288, 0.284, 0.252, 0.220, 0.264, 0.256, 0.232, 0.252, 0.252, 0.264, 0.276, 0.256, 0.240, 0.276, 0.252, 0.272, 0.248, 0.276, 0.236, 0.264, 0.284, 0.264, 0.248, 0.244, 0.280, 0.256, 0.268, 0.264, 0.244, 0.280, 0.280, 0.232, 0.244, 0.256, 0.260, 0.240, 0.256, 0.228, 0.284, 0.244, 0.272, 0.308, 0.292, 0.220, 0.244, 0.244, 0.264, 0.244, 0.244, 0.256, 0.252, 0.252, 0.252, 0.264, 0.284, 0.280, 0.260, 0.248, 0.268, 0.276, 0.308, 0.284, 0.240, 0.228, 0.240, 0.212, 0.260, 0.292]
sor = [sor1, sor2, sor3]
for i in range(len(sor)):
    print(len(sor[i]), sum(sor[i])/len(sor[i]))